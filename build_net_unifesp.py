
import numpy as np
import pickle, sys
from graph_measures import GraphMetric
import igraph

data = pickle.load(open('dados_sjc_lenovo.pk1','rb'))


nomes = []
adj = []
print len(data), 'node_10' in data.keys(),len(data.keys())

#print data.keys()


for k in data.keys():

    nomes.append(data[k]['me'])

    lista = data[k]['adj_list']

    #print lista
    #print data[k]['me'], data.keys().index(k),lista
    no = data.keys().index(k)
    for i in lista:

        if 'node_'+str(i) not in data:
            data.update({'node_' + str(i): {'me': i, 'adj_list': [], 'mylink': ""}})

        adj.append((no,data.keys().index('node_'+str(i))))

g = igraph.Graph(len(data))

#g.vs['names'] = nomes

#nomes.sort()

#print nomes

#print adj
g.add_edges(adj)

igraph.plot(g,layout ="rt",labels =True)