
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

overview = html.Div([
    dbc.Row([
        dbc.Card([
            dbc.CardBody([
                html.H4("How it works", className="card-title"),
                html.P(["""
                    This process for data cleansing focuses on manual entry data. This data will naturally contain typos or alternate spellings.
                    The example on the next tab looks at how this method works with first and last name but can also be expanded to work with
                    addresses or any text based data.
                    """]),
                html.P(["""
                    The foundation for clustering to find fuzzy matches draws it's inspiration from how a person would naturlly look at a list of
                    names to find the nearest match. Close spellings or names that sound the same would be a clue to a normal person. The use of
                    editted distances allows the computer to make similar determinations.
                    """]),
            ]),
        ], className="p-2 mb-2"),
    ]),
    dbc.Row([
        dbc.Card([
            dbc.CardBody([
                html.H4("Data Prep", className="card-title"),
                html.P(["""
                    Let's start by how we clean the data. As with any machine learning algorithm, more information is best! The example on the next tab
                    breaks full names into FirstName & LastName. When using addresses it's often important to break apart the various aspects of it such
                    as street name ("Main") from the street type ("St"). Depending on your distance algorithms it may be necessary to constrict all strings
                    to upper/lower/proper case.
                    """]),
            ]),
        ], className="col-lg p-2 mb-2"),
        dbc.Card([
            dbc.CardBody([
                html.H4("Distance Scores", className="card-title"),
                html.P(["""
                    Go Crazy with distance scores! Compged, Levenshtein, and Jaro are a few readily available algorithms. They score insertions, deletions, or swaps
                    in various ways to determine how different the 2 texts are from each other. Pair those with a soundex algorithm
                    and you are off to an amazing start! The idea behind soundex is to break down
                    segments of text (morphemes) into what it sounds like (phonemes). Because different languages vocalize morphemes differently it can be
                    a monumental task for 1 soundex algorithm. So.... GO CRAZY WITH SOUNDEX ALGORITHMS!
                    """]),
            ]),
        ], className="col-lg p-2 mb-2"),
        dbc.Card([
            dbc.CardBody([
                html.H4("Clustering", className="card-title"),
                html.P(["""
                    The last step where the machine makes a decision for us. This involves clustering the names based on the various editted distances.
                    The clusters will be random, so you need to include the name you are looking for in the list. This leaves us with a target whos editted
                    distances are all 0 because it is an exact match. This also gives us a point of reference to find our cluster that would indicate
                    appropriate matches.
                    """]),
            ]),
        ], className="col-lg p-2 mb-2"),
    ],),
])
