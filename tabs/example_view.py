
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# example_view = dbc.Row([
#     dbc.Card([
#         dbc.CardBody([
#             html.H4("Interactive Example", className="card-title"),
#             html.P(["COMING SOON!"])
#         ]),
#     ], className="col-sm p-2"),
# ])

example_view = dbc.Row([
    dbc.Card([
        dbc.FormGroup([
            dbc.Label("Enter a name below:"),
            dbc.Input(placeholder="Washington, George", type="text", id="entered-name"),
            dbc.FormText("Try a name close to one of the randomly generate names below."),
            dbc.Button("Submit Name", id="submit-name"),
        ]),
        html.Hr(className="my-2"),
        dash_table.DataTable(
            id = 'everyone_else',
            columns=[{'id': c, 'name': c} for c in ['FirstName', 'LastName']],
            fixed_rows={'headers':True},
            style_table={'height': 400}
        ),
        dbc.Button("New Set of Names", id="refresh-list"),

    ], className="col-md-4 p-2"),
    dbc.Col([
        dbc.Card([
            html.P("Let\'s find a match!", id = "input-name"),
        ], className="p-4"),
        dbc.Card([
            dbc.Spinner(
                dcc.Graph(
                    id='example_cluster',
                    config={'displayModeBar': False},
                ),
            )
        ], className="col-md"),
    ]),
],)
