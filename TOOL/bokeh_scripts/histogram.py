# pandas and numpy for data manipulation
import pandas as pd
import numpy as np
import scipy.special

from bokeh.plotting import figure
from bokeh.models import (CategoricalColorMapper, HoverTool, 
						  ColumnDataSource, Panel, 
						  FuncTickFormatter, SingleIntervalTicker, LinearAxis)
from bokeh.models.widgets import (CheckboxGroup, Slider, RangeSlider, 
								  Tabs, CheckboxButtonGroup, 
								  TableColumn, DataTable, Select)
from bokeh.layouts import column, row, WidgetBox
from bokeh.layouts import gridplot
from bokeh.palettes import Category20_16

# Make plot with histogram and return tab
def histogram_tab(flights):

	
	p1 = figure(title="",tools="save",
	            background_fill_color="#E8DDCB")

	hist, edges = np.histogram(flights['LOS'], density=True, bins=50)
	#hist=(hist)*10;
	#x = np.linspace(-2, 2, 1000)
	p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
	        fill_color="#036564", line_color="#033649")
	p1.legend.location = "center_right"
	p1.legend.background_fill_color = "darkgrey"
	p1.xaxis.axis_label = 'LOS'
	p1.yaxis.axis_label = 'Pr(LOS)'
	
	p2 = figure(title="",tools="save",
	            background_fill_color="#E8DDCB")

	hist, edges = np.histogram(flights['classLabel'], density=True, bins=50)
	hist = (hist / flights.shape[0])*10;
	print(hist)
	#x = np.linspace(-2, 2, 1000)
	p2.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
	        fill_color="#036564", line_color="#033649")
	p2.legend.location = "center_right"
	p2.legend.background_fill_color = "darkgrey"
	p2.xaxis.axis_label = 'Expire_Flag'
	p2.yaxis.axis_label = 'Pr(Expire_Flag)'
	

	p=gridplot(p1,p2, ncols=2, plot_width=400, plot_height=400, toolbar_location=None)
	tab = Panel(child=p, title = 'Histogram')

	return tab