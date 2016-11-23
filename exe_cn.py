

import numpy as np
import igraph as gr
import matplotlib.pyplot as plt
from graph_measures import GraphMetric
import time


def exercicio_01():

    t_igraph = []
    t_mygraph = []
    t_vertices = []

    for v in xrange(10,10000,100):

        print 'conta ',v

        g = gr.Graph.GRG(v, 0.5)

        mat = np.zeros((v,v))

        for i in g.get_edgelist():

            mat[i[0],i[1]] +=1

        k = GraphMetric(mat)

        #comentado para rodar somente o igraph (sem comparacao)

        #time_init_a1 = time.time()

        #k.get_degrees(mat)

        #k.get_clustering_coef(mat)

        #t_mygraph.append(time.time() - time_init_a1)

        time_init_a2 = time.time()
        k.get_igraph_measures(g)
        t_igraph.append(time.time() - time_init_a2)
        t_vertices.append(v)


    plt.xlabel('Nodes')
    plt.ylabel('Time')
    #plt.title('Igraph x MyGraph')
    plt.title('Igraph')

    p2 = plt.plot(np.asarray(t_vertices), np.asarray(t_igraph))

    #p1 = plt.plot(np.asarray(t_vertices), np.asarray(t_mygraph))

    #plt.legend([p1[0], p2[0]], ['MyGraph','igraph'])

    plt.legend([p2[0]], [ 'igraph'])

    plt.savefig('Comparativo_igraph.png')

    plt.show()



def exercicio_02(times):

    clustering = []
    diameter = []
    density = []
    degree = []

    #x = [(0, 1), (1, 2), (2, 3), (3, 4)]

    x = [(0,1), (0,2), (0,3)]

    #x = [(0,1), (0,2), (1,2)]

    g1 = gr.Graph(x)

    for i in xrange(times):

        tam = len(g1.vs)-1

        #one
        #g1.add_vertices(1)
        #g1.add_edges([(tam,tam+1)])

        #two
        g1.add_vertices(1)
        g1.add_edges([(0,tam+1)])


        #tree
        '''
        a = g1.neighborhood(tam)

        g1.delete_edges([(tam,a[len(a)-1])])

        g1.add_vertices(1)

        g1.add_edges([(tam,tam+1), (a[len(a)-1], tam+1)])
        '''
        clustering.append(np.mean(np.asarray(g1.transitivity_local_undirected(mode='zero'))))

        diameter.append(g1.diameter())

        density.append(g1.density())

        degree.append(np.mean(np.asarray(g1.degree())))

    gr.plot(g1)

    return diameter, density, degree, clustering


def exercicio_03():

    x = [(0,1),(0,2),(0,3),(1,2),(3,2),(4,3)]

    g= gr.Graph(x)

    g.vs['label'] = ['0','1','2','3','4','5']

    #gr.add_edges(x)

    gr.plot(g, labels =True)


def get_subplots(diameter, density, degree, clustering):

    f, ((p1,p2),(p3, p4)) = plt.subplots(2,2, sharex='col',sharey='row')

    p1.plot(np.asarray(diameter))
    p1.set_title('Diameter')

    p2.plot(np.asarray(density))
    p2.set_title('Density')
    p2.set_ylim(ymin=-1)


    p3.plot(np.asarray(degree))
    p3.set_title('Degree')
    p3.set_ylim(ymin=-1, ymax=np.max(np.asarray(degree))+2)

    p4.plot(np.asarray(clustering))
    p4.set_title('Clustering')
    p4.set_ylim(ymin=-1)

    #plt.xlabel('Nodes')
    #plt.ylabel('Time')
    #plt.title('Igraph x MyGraph')
    #print 'asd', degree
    plt.show()


exercicio_01()

#a,b,c,d = exercicio_02(1000)

#get_subplots(a,b,c,d)
