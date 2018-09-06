import os
import pandas as pd
import config
import numpy as np

from mod_datacleaning import data_cleaning
import heidicontroller_helper as hch

from mod_matrix import generateCustomMatrix as gcm
from mod_matrix import region_label as rg
from mod_matrix import image_module as hd
from mod_matrix import orderPoints as op

from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.plotting import figure, output_file, show
from bokeh.models.widgets import Panel, Tabs
from bokeh.layouts import gridplot


from bokeh_scripts.histogram import histogram_tab
from bokeh_scripts.density import density_tab
from bokeh_scripts.table import table_tab
from bokeh_scripts.draw_map import map_tab
from bokeh_scripts.routes import route_tab
from bokeh.models.widgets import Slider, TextInput
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource

# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value


def update_data(attrname, old, new):

    # Get the current slider values
    a = amplitude.value
    b = offset.value
    w = phase.value
    k = freq.value

    # Generate the new curve
    x = np.linspace(0, 4*np.pi, N)
    y = a*np.sin(k*x + w) + b

    source.data = dict(x=x, y=y)


def getMetaInfo(data):
	'''
	cname=list(data.columns)
	for c in cname:
		if c.find('ID')==-1:
			print(c)
	data = {"y": [1, 2, 3, 4, 5]}
	output_file("lines.html", title="line plot example") #put output_notebook() for notebook
	# Here is a list of categorical values (or factors)
	fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']

	# Set the x_range to the list of categories above
	p = figure(x_range=fruits, plot_height=250, title="Fruit Counts")

	# Categorical values can also be used as coordinates
	p.vbar(x=fruits, top=[5, 3, 4, 2, 4, 6], width=0.9)

	# Set some properties to make the plot look better
	p.xgrid.grid_line_color = None
	p.y_range.start = 0
	'''

	
	# Read data into dataframes
	flights = pd.read_csv('static/flights.csv',index_col=0).dropna()
	# Formatted Flight Delay Data for map
	map_data = pd.read_csv('static/flights_map.csv',header=[0,1], index_col=0)

	tab1 = histogram_tab(data)
	tab2 = density_tab(data)
	tab3 = table_tab(data)
	#tab4 = map_tab(map_data, states)
	#tab5 = route_tab(flights)

	# Put all the tabs into one application
	tabs = Tabs(tabs = [tab1,tab2,tab3])
	return tabs
	'''
	# Set up data
	N = 200
	x = np.linspace(0, 4*np.pi, N)
	y = np.sin(x)
	source = ColumnDataSource(data=dict(x=x, y=y))


	# Set up plot
	plot = figure(plot_height=400, plot_width=400, title="my sine wave",
	              tools="crosshair,pan,reset,save,wheel_zoom",
	              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

	plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


	# Set up widgets
	offset = Slider(title="offset", value=0.0, start=-5.0, end=5.0, step=0.1)
	amplitude = Slider(title="amplitude", value=1.0, start=-5.0, end=5.0, step=0.1)
	phase = Slider(title="phase", value=0.0, start=0.0, end=2*np.pi)
	freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1, step=0.1)

	
	for w in [offset, amplitude, phase, freq]:
		w.on_change('value', update_data)


	# Set up layouts and add to document
	inputs = widgetbox( offset, amplitude, phase, freq)

	tabs = row(inputs, plot, width=800)
	return tabs
	'''