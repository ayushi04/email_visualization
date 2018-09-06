# pandas and numpy for data manipulation
import pandas as pd
import numpy as np

from scipy.stats import gaussian_kde

from bokeh.plotting import figure
from bokeh.models import (CategoricalColorMapper, HoverTool, 
						  ColumnDataSource, Panel, 
						  FuncTickFormatter, SingleIntervalTicker, LinearAxis)
from bokeh.models.widgets import (CheckboxGroup, Slider, RangeSlider, 
								  Tabs, CheckboxButtonGroup, 
								  TableColumn, DataTable, Select)
from bokeh.layouts import column, row, WidgetBox
from bokeh.palettes import Category20_16

def density_tab(data):
	
	print('---------------------------------------------')
	print(data.columns,data.shape[0])
	carrier_stats = {}
	index=[]
	val=[]
	carrier_stats['Total Number of ICU Patients']=data.shape[0]
	carrier_stats['Total Number of ICU surivors']=data[data['classLabel']==0].shape[0]
	t=list(data['LABEL'])
	x=[str(i).split(':') for i in t ]
	t = [item for sublist in x for item in sublist]
	#print(t)
	from collections import defaultdict
	fq= defaultdict(int)
	for w in t:
	    fq[w] += 1
	print(fq)
	print(sorted(fq, key=fq.get, reverse=True))
	carrier_stats['Top 5 frequent inputs given to ICU patients'] = sorted(fq, key=fq.get, reverse=True)[:5]
	carrier_stats=pd.DataFrame(list(carrier_stats.items()), columns=['index1', 'value'])
	print(carrier_stats)
	
	carrier_src = ColumnDataSource(carrier_stats)
	table_columns = [TableColumn(field='index1', title='index'),TableColumn(field='value', title='Expire_Flag')]
	carrier_table = DataTable(source=carrier_src,columns=table_columns,width=1000)
	tab = Panel(child = carrier_table, title = 'Data Desciption')
	return tab
	return ""