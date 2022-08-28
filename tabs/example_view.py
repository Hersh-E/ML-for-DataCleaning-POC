
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash import dash_table

# example_view = dbc.Row([
#     dbc.Card([
#         dbc.CardBody([
#             html.H4("Interactive Example", className="card-title"),
#             html.P(["COMING SOON!"])
#         ]),
#     ], className="col-sm p-2"),
# ])

example_view = dbc.Row([
    dbc.Col([
        dbc.Card([
            dbc.Label("Enter a name below:"),
            dbc.Input(placeholder="Washington, George", type="text", id="entered-name"),
            dbc.FormText("Try a name close to one of the randomly generate names below."),
            dbc.Button("Submit Name", id="submit-name"),
            html.Hr(className="my-2"),
            dash_table.DataTable(
                id = 'everyone_else',
                columns=[{'id': c, 'name': c} for c in ['FirstName', 'LastName']],
                fixed_rows={'headers':True},
                style_table={'height': 400}
            ),
            dbc.Button("New Set of Names", id="refresh-list"),

        ], className="p-2"),
    ], className="px-0", lg=3),

    dbc.Col([
        dbc.Card([
            html.P("Let\'s find a match!", id = "input-name"),
        ], className="p-4", style={'height':'15%'}),
        dbc.Card([
            dbc.Spinner(
                dcc.Graph(
                    id='example_cluster',
                    config={'displayModeBar': False},
                ),
            )
        ], className="col-md", style={'height':'85%'}),
    ], className="px-0", lg=9),

])
