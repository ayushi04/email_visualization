# pandas and numpy for data manipulation
import pandas as pd
import numpy as np

from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import TableColumn, DataTable

def table_tab(data):

	# Calculate summary stats for table
	print('---------------------------------------------')
	print(data.columns)
	carrier_stats = data[['LOS','HOURS','GENDER','classLabel']].describe()
	carrier_stats = carrier_stats.reset_index()
	carrier_stats.columns=['index1', 'LOS', 'HOURS', 'classLabel']
	
	carrier_src = ColumnDataSource(carrier_stats)

	# Columns of table
	table_columns = [TableColumn(field='index1', title='index'),
					 TableColumn(field='LOS', title='Duration of ICU stay'),
					 TableColumn(field='HOURS', title='Hours'),
					 TableColumn(field='classLabel', title='Expire_Flag')]
	
	#carrier_src=carrier_stats.reset_index()
	#print(carrier_src)
	carrier_table = DataTable(source=carrier_src,columns=table_columns,width=1000)
	#carrier_table={}
	tab = Panel(child = carrier_table, title = 'Summary Table')

	return tab