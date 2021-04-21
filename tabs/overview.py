
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

overview = dbc.Row([
    dbc.Card([
        dbc.CardBody([
            html.H4("Data Prep", className="card-title"),
            html.P(["Text about how to cleanse"])
        ]),
    ], className="col-lg p-2 mb-lg-0 mb-2"),
    dbc.Card([
        dbc.CardBody([
            html.H4("Distance Scores", className="card-title"),
            html.P(["Text about how to score"])
        ]),
    ], className="col-lg p-2 mb-lg-0 mb-2"),
    dbc.Card([
        dbc.CardBody([
            html.H4("Clustering", className="card-title"),
            html.P(["Recieving results from the cluster"])
        ]),
    ], className="col-lg p-2 mb-lg-0 mb-2"),
],)
