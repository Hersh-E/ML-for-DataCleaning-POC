
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import pandas as pd
import numpy as np
from datetime import datetime
import pathlib

from funcs.compged import compged
from funcs.cluster_func import cluster_func
import fuzzy
import Levenshtein as lev
import names as name_gen

from app import app
from app import application

from tabs.overview import overview
from tabs.example_view import example_view
from tabs.considerations_view import considerations
from tabs.about_view import about

server = app.server

app.layout = html.Div([
    html.Div(
        dbc.Container([
    		html.H1("Using Machine Learning to Cleanse Data", className="display-3"),
    		html.P("This is a proof of concept on how clustering can help cleanse manual entry data", className="lead"),
    		html.Hr(className="my-2"),
    		html.P([
    			"Read the below guide for how this proof of concept works.", html.Br(),
    			"Check out the interactive example on the following tab.", html.Br(),
    			"Lastly, go over the considerations. This is only a proof of concept after all."
    		]),
    	], className='py-3'),
    className="p-3 bg-light rounded-3"),
	# Tab Line
    dbc.Container([
    	dbc.Row([
    		dbc.Tabs([
    			dbc.Tab(label="Overview", tab_id="overview"),
    			dbc.Tab(label="Example", tab_id="example"),
    			dbc.Tab(label="Considerations", tab_id="considerations"),
    			dbc.Tab(label="About", tab_id="about"),
    		], id='tabs', active_tab="overview"),
			html.Hr(className="mb-0 px-0 pb-0"),
		], className='pt-3'),
	], className='',),
	# Info Cards
	# dbc.Container([], id="content", style={'padding':0}, className="tab-content"),
	dbc.Container([], id="content", className="tab-content"),
	# hidden div to hold the name data
	html.Div(id='name-list', style={'display':'none'}),
	# <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
	# html.Script(src="https://platform.linkedin.com/badges/js/profile.js", defer=True, type="text/javascript", **{'async':True, })
])

@app.callback([Output("content", "children")], [Input("tabs", "active_tab")])
def switch_tab(at):
	if at == "overview":
		content = overview
	elif at == "example":
		content = example_view
	elif at == "considerations":
		content = considerations
	elif at == "about":
		content = about
	return [content]

# @app.callback(Output("input-name","children"),[Input("submit-name", "n_clicks"), State("entered-name", "value")])
# def show_Name(n, name):
# 	if name == None:
# 		return "I'll show you the name you entered."
# 	elif name == "":
# 		return "Please enter a name."
# 	else:
# 		return "You submitted the name: {}.".format(name)

@app.callback([Output("example_cluster","figure"), Output("input-name","children")],[Input("entered-name", "n_submit"), Input("submit-name", "n_clicks"), State("entered-name", "value"), State("name-list", 'children')])
def update_cluster_graph(n1, n2, name, namelist_json):
	if name == None:
		return dash.no_update
	elif name == "":
		return dash.no_update
	else:
		namelist = pd.read_json(namelist_json, orient='split').reset_index()

		results_df, matches = cluster_func(name, namelist)

		fig = px.scatter(results_df, x='x', y='y', color='hue', size='size', hover_data={'x':False, 'y':False, 'hue':False, 'size':False, 'FirstName':True, 'LastName':True})

		fig.update_xaxes(fixedrange=True, visible=False)
		fig.update_yaxes(fixedrange=True, visible=False)

		if matches == 1:
			response = 'You\'re too unique!'
		else:
			response = 'Looks like we found a Match!'

		return fig, response

@app.callback(
	Output('name-list', 'children'),
	[Input('refresh-list', 'n_clicks')],
)
def generate_values(n_clicks):
	 # some expensive clean data step
	namelist = pd.DataFrame({'FirstName' : [name_gen.get_first_name() for x in range(50)],
		'LastName' : [name_gen.get_last_name() for x in range(50)]})
	return namelist.to_json(date_format='iso', orient='split')

@app.callback(
	Output('everyone_else', 'data'),
	[Input('name-list', 'children')],
)
def generate_values(namelist_json):
	 # some expensive clean data step
	namelist = pd.read_json(namelist_json, orient='split').reset_index()

	return namelist.to_dict('records')



if __name__ == '__main__':

	app.run_server(debug=True, processes=1, threaded=True, host='127.0.0.1', port=8050, use_reloader=True)
	# app.run_server()
