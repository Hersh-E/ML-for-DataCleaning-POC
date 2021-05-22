
import pandas as pd
import fuzzy
import numpy as np
import Levenshtein as lev
from sklearn.cluster import AgglomerativeClustering
import names as name_gen
from funcs.compged import compged
from sklearn.decomposition import PCA


def scale_it(var, table, list):
    table['scaled_{}'.format(var)] = (table[var] - np.mean(table[var])) / np.std(table[var])
    list.append('scaled_{}'.format(var))

# namelist = pd.DataFrame({'FirstName' : [name_gen.get_first_name() for x in range(50)],
#     'LastName' : [name_gen.get_last_name() for x in range(50)]})
#
# firstname = 'Hershel'
# lastname = 'Eason'
# firstname.title()

def cluster_func(name, PeopleVerse):
    if name.find(',') > 0:
        lastname, firstname = [x.strip().title() for x in name.split(',')]
    else:
        firstname, lastname = [x.strip().title()  for x in name.split()]

    focus = pd.DataFrame([[firstname, lastname]], columns=['FirstName', 'LastName'])

    PeopleVerse = PeopleVerse.append(focus, ignore_index=True)

    PeopleVerse['X1'] = PeopleVerse.FirstName.apply(lambda x: compged(firstname, x))
    PeopleVerse['X2'] = PeopleVerse.LastName.apply(lambda x: compged(lastname, x))
    PeopleVerse['X3'] = PeopleVerse.FirstName.apply(lambda x: compged(fuzzy.nysiis(firstname), fuzzy.nysiis(x)))
    PeopleVerse['X4'] = PeopleVerse.LastName.apply(lambda x: compged(fuzzy.nysiis(lastname), fuzzy.nysiis(x)))
    PeopleVerse['X5'] = PeopleVerse.FirstName.apply(lambda x: lev.jaro(x, firstname))
    PeopleVerse['X6'] = PeopleVerse.LastName.apply(lambda x: lev.jaro(x, lastname))
    PeopleVerse['X7'] = PeopleVerse.FirstName.apply(lambda x: lev.jaro(fuzzy.nysiis(x), fuzzy.nysiis(firstname)))
    PeopleVerse['X8'] = PeopleVerse.LastName.apply(lambda x: lev.jaro(fuzzy.nysiis(x), fuzzy.nysiis(lastname)))

    fit_on = []

    scale_it('X1', PeopleVerse, fit_on)
    scale_it('X2', PeopleVerse, fit_on)
    scale_it('X3', PeopleVerse, fit_on)
    scale_it('X4', PeopleVerse, fit_on)
    scale_it('X5', PeopleVerse, fit_on)
    scale_it('X6', PeopleVerse, fit_on)
    scale_it('X7', PeopleVerse, fit_on)
    scale_it('X8', PeopleVerse, fit_on)

    model = AgglomerativeClustering(linkage='complete', connectivity=None, n_clusters=5)
    model.fit(PeopleVerse[fit_on])

    PeopleVerse['Cluster'] = model.labels_

    cluster = PeopleVerse.loc[(PeopleVerse['FirstName'] == firstname) & (PeopleVerse['LastName'] == lastname)]['Cluster'].iat[0]
    matches = PeopleVerse.loc[PeopleVerse['Cluster'] == cluster, ['FirstName','LastName']].shape[0]

    pca = PCA(n_components = 2)
    PeopleVerse[['x', 'y']] = pd.DataFrame(pca.fit_transform(PeopleVerse[fit_on]),columns=['x','y'])
    PeopleVerse['hue'] = PeopleVerse['Cluster'].apply(lambda x: 'you' if x == cluster else 'everyone else')
    PeopleVerse['size'] = PeopleVerse['Cluster'].apply(lambda x: 5 if x == cluster else 1)

    return [PeopleVerse[['FirstName', 'LastName', 'x', 'y', 'hue', 'size']], matches]



# name = 'hershel eason'
#
# namelist = pd.DataFrame({'FirstName' : [name_gen.get_first_name() for x in range(50)],
#     'LastName' : [name_gen.get_last_name() for x in range(50)]})
#
# results_df, matches = cluster_func(name, namelist)
# fig = px.scatter(results_df, x='x', y='y', color='hue', size='size', custom_data=['FirstName', 'LastName'])
#
# fig.update_traces(hovertemplate='%{custom_data[0]} %{custom_data[1]}')
#
# fig
# 
# import plotly.express as px
#
#
# dir(fig)
#
# fig.data[1]
# fig.update_traces(marker=dict(size=12,
#                               line=dict(width=2,
#                                         color='DarkSlateGrey')),
#                   selector=dict(mode='markers'))
# fig
