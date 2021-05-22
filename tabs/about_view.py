
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pathlib

asset_path = pathlib.Path(__file__).parent.parent.joinpath("assets").resolve()

about = html.Div([
    dbc.Row([
        dbc.Card([dbc.CardImg(src='../assets/Profile-Pic.png', top=True)], "p-2 mb-2 col-lg"),
        # html.P([str(asset_path.joinpath('Profile-Pic.png'))]),
        dbc.Card([
            dbc.CardBody([

                html.H4("About the Author", className="card-title"),

                html.P(["""
                    Hershel Eason is a data insights enthusiast. Machine learning, interactive dashboards (like this one built using Plotly Dash),
                    and boatloads of creativity allow hershel to tackle real world problems in innovative ways.
                    """]),
                html.P(["""
                    Data is cool, but what data tells us is insight. What we do with that insight defines growth.
                    """]),
                html.P([
                    """If you like this proof of concept and want to connect with or follow Hershel, check him out on """,
                    html.A('LinkedIn', href="https://www.linkedin.com/in/hersheleason/"),
                    """ and stay tuned for more articles on """,
                    html.A('Medium', href="https://medium.com/@hersheleason/"),
                    """.""",
                ]),
            ]),
        ], className="p-2 mb-0 col-lg"),
    ]),
])
