
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

considerations = dbc.Row([
    dbc.Card([
        dbc.CardBody([
            html.H4("Some thoughts to consider:", className="card-title"),
            html.P(["1. This algorithm works for 1 name at a time. When cleaning large sets of data this can be a real constraint. However, once all the data is clean this presents a very small consideration in a multithreaded pipeline."]),
            html.P(["2. Country of origin and language matter with soundex algorithms. This makes them not a one-size-fits-all. Ideally, you'd be able to swap out algorithms based on the seed name's origin. Still, any soundex is usually better than no soundex."]),
            html.P(["3. The vanilla agglomerative clustering algorithm is quite resource intensive and presents a major consideration for medium to large datasets. There are ways to shrink it down such as limiting to closest 10k points."]),
            html.P(["4. Not all distances are created equal. The right balance of edit distances are important and will change for names, addresses, or any other data point."]),
        ]),
    ], className="col-sm p-2"),
])
