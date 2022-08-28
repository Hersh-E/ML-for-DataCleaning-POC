
import dash
import dash_bootstrap_components as dbc
import os

# app = dash.Dash("ML for Data Cleaning: A POC", external_stylesheets=[dbc.themes.YETI], suppress_callback_exceptions=True, external_scripts=['https://platform.linkedin.com/badges/js/profile.js'])
app = dash.Dash("ML for Data Cleaning: A POC", external_stylesheets=[dbc.themes.FLATLY], suppress_callback_exceptions=True)

application = app.server
