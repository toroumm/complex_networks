

import numpy as np
import igraph as gr
import matplotlib.pyplot as plt
from graph_measures import GraphMetric
import time


def exercicio_01():

    t_igraph = []
    t_mygraph = []

    for v in xrange(10,1000,200):

        print 'conta ',v

        g = gr.Graph.GRG(v, 0.5)

        mat = np.zeros((v,v))

        for i in g.get_edgelist():

            mat[i[0],i[1]] +=1

        k = GraphMetric(mat)

        time_init_a1 = time.time()

        k.get_degrees(mat)

        k.get_clustering_coef(mat)

        t_mygraph.append(time_init_a1 - time.time())

        time_init_a2 = time.time()
        k.get_igraph_measures(g)
        t_igraph.append(time_init_a2-time.time())


    plt.xlabel('Nodes')
    plt.ylabel('Time')
    plt.title('Igraph x MyGraph')


    p2 = plt.plot( np.asarray(t_igraph))

    p1 = plt.plot(np.asarray(t_mygraph))

    plt.legend([p1[0], p2[0]], ['MyGraph','igraph'])

    plt.savefig('Comparativo_igraph.png')

    plt.show()

exercicio_01()

def exercicio_02(times):

    clustering = []
    diameter = []
    density = []
    degree = []

    #x = [(0, 1), (1, 2), (2, 3), (3, 4)]

    #x = [(0,1), (0,2), (0,3)]

    x = [(0,1), (0,2), (1,2)]

    g1 = gr.Graph(x)

    for i in xrange(times):

        tam = len(g1.vs)-1

        #one
        #g1.add_edges([(tam,tam+1)])

        #two
        #g1.add_edges([(0,tam+1)])

        #tree
        a = g1.neighborhood(tam)

        g1.delete_edges([(tam,a[len(a)-1])])

        g1.add_vertices(1)

        g1.add_edges([(tam,tam+1), (a[len(a)-1], tam+1)])

        clustering.append(np.mean(np.asarray(g1.transitivity_local_undirected(mode='zero'))))

        diameter.append(g1.diameter())

        density.append(g1.density())

        degree.append(np.mean(np.asarray(g1.degree())))

    #gr.plot(g1)

    return clustering,diameter,density,degree


def exercicio_03():

    x = [(0,1),(0,2),(0,3),(1,2),(1,4),(4,5)]

    g= gr.Graph(x)

    g.vs['label'] = ['0','1','2','3','4','5']

    #gr.add_edges(x)

    gr.plot(g, labels =True)

