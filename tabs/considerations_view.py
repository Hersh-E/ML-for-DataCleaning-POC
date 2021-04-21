
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

considerations = dbc.Row([
    dbc.Card([
        dbc.CardBody([
            html.H4("Considerations", className="card-title"),
            html.P(["COMING SOON!"])
        ]),
    ], className="col-sm p-2"),
])
