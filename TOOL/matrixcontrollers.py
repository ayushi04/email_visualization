from flask import request, render_template, Blueprint, json, redirect, url_for, flash
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, current_user, logout_user
import random
import os
import pandas as pd
import config
import math
from mod_datacleaning import data_cleaning
import heidicontroller_helper as hch
from models import ImageDB,Legend,TopLegend,ImageInfo
import numpy as np

from mod_matrix import generateCustomMatrix as gcm
from mod_matrix import region_label as rg
from mod_matrix import image_module as hd
from mod_matrix import orderPoints as op
from mod_matrix import database_mysql as dbc

from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.embed import components
from bokeh.util.string import encode_utf8
from bokeh.resources import INLINE

import linecache
import sys
def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
    return ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

mod_matrixcontrollers = Blueprint('matrixcontrollers', __name__)

@mod_matrixcontrollers.route('/data_filter',methods=['POST','GET'])
def data_filter():
    print('-----data_filter------')
    if request.method == 'POST':
        #try:
            datasetPath=request.form['datasetPath']
            #user = User(request.form['name'], request.form['phone'], generate_password_hash(request.form['password'], method='sha256'), request.form['email'])
            print(datasetPath)
            gender=request.form.getlist('gender')
            los=request.form.getlist('los')
            age=request.form.getlist('age')
            icd9=request.form.getlist('icd9');
            print('gender: %s, los : %s, age : %s, icd9 category code : %s' %(gender,los,age,icd9))
            x=pd.read_csv(filepath_or_buffer=datasetPath, sep=',',index_col='id', parse_dates=True)
            print(x.shape)
            '''#4sep
            if 'ALL' not in gender:
                x=x[x.GENDER.isin(gender)]
            if 'ALL' not in los:
                x=x[x.LOS.isin(los)]
            #if 'ALL' not in age:
            #    x=x[x.AGE.isin(age)]
            if 'ALL' not in icd9:
                x=x[x.ICD9_CATEGORY.isin(icd9)]
            '''#4sep

            print(x.shape)
            filename='filteredData.csv'
            file_uploads_path = os.path.join(config.UPLOADS_DIR, filename)
            x.to_csv(file_uploads_path, sep=',',index=True)
            datasetPath = 'static/uploads/' + filename
            #db.session.add(user)
            #db.session.commit()
            #GENERATING META-INFORMATION OF DATA
            '''#4sep
            plot=hch.getMetaInfo(x)
            html=file_html(plot,CDN,"my plot")
            file = open("static/output/myhtml.html","w") 
            file.write(html)
            file.close()
            '''#4sep
            #print(script,div)
            return render_template('data_analysis.html',title='visual tool',datasetPath=datasetPath, user=current_user)
            return "123"
            #return redirect(url_for('matrixcontrollers.image'))
        #except Exception as e:
        #    print(e)
        #    flash('Wrong inputs, please check your input and try again.')
        #    return render_template('data_filter.html', user=current_user, datasetPath='static/uploads/V3_ICU_INPUT_NAME_PATIENT_ICD9_less.csv')


@mod_matrixcontrollers.route('/image',methods=['POST','GET'])
def image():
    #print('----matrixcontrollers: image---')
    #try:
        datasetPath=request.args.get('datasetPath')
        equations=request.args.get('equations')
        equations=equations.split(':')
        print('INPUT PARAMS : datasetPath: %s, equations: %s' %(datasetPath,equations))
        inputData = pd.read_csv(filepath_or_buffer=datasetPath,sep=',',index_col='id', parse_dates=True)
        #print(inputData.dtypes)
        
        #FILTEREDDATA
        order_dim=['classLabel']
        datelist=['DOB','DOD','DOD_HOSP','DOD_SSN']
        '''#4sep
        for c in datelist:
            inputData[c]=pd.to_datetime(inputData[c], errors='ignore')
        '''#4sep
        for eq in equations:
            t=gcm.mysplit(eq)
            #print(t)
            for i in t:
                if(i in inputData.columns and i not in order_dim and i not in datelist and i !='ICD9_CATEGORY' and i!='INPUTS'):
                    order_dim.append(i)
        order_dim=['topic1','topic2','topic3','topic4','topic5','topic6','topic7','topic8','topic9','topic10','classLabel'] # 4sep
        print('------order_dim-----',order_dim)
        filtered_data = inputData.loc[:,order_dim]
        filtered_data['classLabel_orig']=filtered_data['classLabel'].values
        #ORDER POINTS
        # IF ORDERDIM LENGTH =1 THEN ORDERING BY SORTED ORDER ELSE SOME OTHER ORDERING SCHEMA
        if len(order_dim)==1:
            param={}
            param['columns']=list(filtered_data.columns[:-1])
            param['order']=[True for i in param['columns']]
            sorted_data=op.sortbasedOnclassLabel(filtered_data,'dimension',param)
            # REINDEXING THE INPUT DATA (TO BE USED LATER)
            sorting_order=sorted_data.index
            inputData=inputData.reindex(sorting_order)
        else:
            print('mst ordering')
            param={}
            sorted_data=op.sortbasedOnclassLabel(filtered_data,'pca_ordering',param)#'mst_distance' #connected_distance knn_bfs
            #sorted_data=op.sortbasedOnclassLabel(filtered_data,'euclidian_distance',param)
            sorting_order=sorted_data.index
            inputData=inputData.reindex(sorting_order)
        inputData.to_csv('static/output/sortedData.csv')
        print('----succesfully ordered points----')
        #CALL CODE TO GET CUSTOM IMAGE FROM DATASET AND BIT VECTOR 
        c= gcm.generateCustomMatrix()
        c.resetBitList()
        for eq in equations:
            c.appendToBitList([eq])
        print("shape of inputData to the matrix:", inputData.shape)
        matrix,bs = c.generateCustomHeidiMatrix(inputData)
        print("shape of matrix generated:",matrix.shape)
        print('----matrix generated ---')
        #lbl=rg.regionLabelling_8(matrix)
        #print('---region labelling done ---')
        #tmp=pd.DataFrame(lbl)
        tmp=pd.DataFrame(matrix)
        output='static/output'
        img,bit_subspace=hd.generateHeidiMatrixResults_noorder_helper(matrix,bs,output,inputData,'legend_heidi')
        
        print('--generated image ---')
        #4sep
        lbl=np.zeros((matrix.shape[0],matrix.shape[1]))#rg.regionLabelling_8(matrix)
        print('--region labelling done ---')
        output='static/output'
        #SAVE IMAGE IN DATABASE
        dbc.deleteAllNodes(labelname='image')    
        dbc.saveMatrixToDatabase_leaf(img,bit_subspace,output,inputData,lbl,labelname='image')
        dbc.saveColorToDatabase(bit_subspace,'image')
        x=list(filtered_data['classLabel'].values)
        dbc.saveClassLabelColorsInDatabase('image',list(set(x)))
        inputData.to_csv('static/output/sortedData.csv')
        l=[]
        label=[]
        for i in set(x):
            c=x.count(i)
            l.append(c)
            label.append(i)
        l=','.join([str(i) for i in l])
        label=','.join([str(i) for i in label])
        dbc.saveInfoToDatabase(img.size[0],img.size[1],'image',l,label)
        
        #READ IMAGE FROM DATABASE
        pixels=dbc.databasefilter(labelname='image',color='ALL')
        
        width,height,scale,class_count,class_label=dbc.getImageParams('image')
        print('getImageParams',width,height,scale,class_count,class_label)
        class_count=class_count.split(',')
        perclustercount=[int(i) for i in class_count]
        class_label=class_label.split(',')
        class_label=[int(i) for i in class_label]
        #print('pppp1',width,height,scale)
        color_dict=dbc.getColorFromTopLegend('image')
        print(color_dict)
        img=dbc.drawImage(pixels,width,height,scale,perclustercount,class_label,color_dict,grid=True)
        
        dbc.updateImageInfo(img.size[0],img.size[1],'image') #LEGEND SPACING AND OTHER STUFF
        #4sep
        
        output='static/output'
        filename='consolidated_img.png'
        img.save(output+'/'+filename)        #SAVE DATASET IN DATABASE (OPTIONAL)
        #SAVE IMAGE IN OUTPUT DIRECTORY
        return json.dumps({'output':str(123),'subspace':str("123")})
    #except Exception as e:
    #    print(e)
    #    flash(e)
    #    datasetName=request.args.get('datasetPath')
    #    return render_template('data_analysis.html',user=current_user,datasetPath=datasetPath)

@mod_matrixcontrollers.route('/highlightPattern',methods=['POST','GET'])
def highlightPattern():
    print('-- highlightPattern-- ')
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    grid=False
    gridwisePattern=True
    datasetPath = 'static/output'
    datasetName = 'image'
    print(x,y,datasetPath,datasetName)
    width,height,scale,class_count,class_label=dbc.getImageParams(datasetName)
    tx = ImageInfo.query.filter_by(name='image')
    w,h=tx[0].with_legend_width,tx[0].with_legend_height
    class_count=class_count.split(',')
    perclustercount=[int(i) for i in class_count]
    class_label=class_label.split(',')
    class_label=[int(i) for i in class_label]
    x=(x*w)/(scale)
    y=(y*h)/(scale)
    #print(x-1,y-1)
    x=int(math.ceil(x))
    y=int(math.ceil(y))
    t=y
    y=x
    x=t
    print(x,y)
    tlx,tly,block_row,block_col=dbc.getTopLeftCoordinates_Grid(x-1,y-1,labelname='image')
    print('TOP lEFT COORDINATES: ',tlx,tly)
    
    if(gridwisePattern==True):
        pixels,color=dbc.blockfilter(x-1,y-1,labelname='image')
    else:
        pixels,color=dbc.databasepatternfilter(x-1,y-1,labelname='image')

    
    #subspace=dbc.getColorSubspace(color,datasetName.split('.')[0]+imgType)
    print(color)
    tx=Legend.query.filter_by(name='image',color=color[1:])

    print('subspaceeee',tx[0].subspace)
    
    img=rg.visualize_regions_v2(pixels,width,height,scale)
    img.save('static/output/temp.png')
    #sortedData=pd.read_csv('static/output/sortedData.csv',index_col='id')
    sortedPath='static/output/sortedData.csv'
    rp,cp=dbc.getCoordinates(pixels,sortedPath,unique=True)
    print(rp,cp)
    rp.to_csv('static/output/rowPoints.csv')
    cp.to_csv('static/output/colPoints.csv')
    return json.dumps({})
    
@mod_matrixcontrollers.route('/visualDashboard')
def visualDashboard():
    print('--visualDashboard--')
    
    color = request.args.get('color_value')
    datasetName=os.path.basename(request.args.get('datasetPath'))
    
    pixels_b1 = ImageDB.query.filter_by(name='image',block_col=0,block_row=0,color=color)
    pixels_b2 = ImageDB.query.filter_by(name='image',block_col=1,block_row=1,color=color)
    
    sortedPath='static/output/sortedData.csv'
    rp_b1,cp_b1=dbc.getCoordinates(pixels_b1,sortedPath,unique=True)
    rp_b2,cp_b2=dbc.getCoordinates(pixels_b2,sortedPath,unique=True)
    
    _,_,_,class_count,_=dbc.getImageParams('image')
    class_count=class_count.split(',')
    print(rp_b1.shape,' ',cp_b1.shape,' ',rp_b2.shape,' ',cp_b2.shape," ",class_count)
    x=pd.read_csv('static/output/sortedData.csv')
    #return ""
    return json.dumps({'b1':rp_b1.shape[0],'b2':rp_b2.shape[0],'b1_s':int(class_count[0]),'b2_s':int(class_count[1])})