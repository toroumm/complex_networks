	

import numpy as np
import igraph
import time


class GraphMetric:

	def __init__(self, _adj_mat = 0):
		
		self.degree_hist = 0
		self.degree_mat = 0
		self.degree_avg = 0
		self.order = 0
		self.length = 0
		self.adj_list = []
		self.adj_mat = _adj_mat
		self.clustering_avg = 0
		self.clustering_mat = 0
		self.properties = {'weighted':0,'simple':1,'directed':0}

############################################################################

	def get_igraph_measures(self, graph):

		measures = {}

		measures.update({'degree':graph.degree()}) #grau do vertice
		measures.update({'degree_avg':np.mean(np.asarray(graph.degree()))}) #grau medio do grafo
		measures.update({'clustering_coefficient': graph.transitivity_local_undirected()})  # coeficiente de aglomeracao, a probabilidade de meus vizinhos serem vizinhos entre eles

		'''
		measures.update({'edge_betweenness':graph.edge_betweenness()}) #quantos caminhos mais proximo de vertice a vertice passam por cada vertice
		measures.update({'short_paths':graph.get_shortest_paths()}) # menor caminho vertice a vertice
		measures.update({'diameter':graph.get_diameter()})
		measures.update({'density':graph.density()})
		'''
		return measures

	def get_measures(self, mat):

		self.set_adj_mat(mat)

		self.get_degrees(mat)

		self.get_clustering_coef(mat)
		

############################################################################


	def set_adj_mat(self, _mat):
		self.adj_mat = np.copy(_mat)

############################################################################

	def get_shortest_path(self):

		names= np.arange(1,self.order+1).tolist()
		
		g = igraph.Graph.Adjacency(self.adj_mat.tolist(), mode= igraph.ADJ_UNDIRECTED)

		g.es['weight'] = self.adj_mat[np.nonzero(self.adj_mat)]
		g.vs['label'] = names

		_list = []

		for i in xrange(self.adj_mat.shape[0]):

			_list.append(igraph.GraphBase.get_all_shortest_paths(g,i))

		igraph.plot(g, layout="rt", labels = True)
		
		return _list 
############################################################################

	def cout(self):
		
		print 'degree hist ',self.degree_hist
		print 'degree mat ',self.degree_mat
		print 'degree avg ',self.degree_avg
		print 'order ',self.order
		print 'lenght ',self.length
		print 'adj_mat ',self.adj_mat 
		print 'custering mat ',self.clustering_mat
		print 'custering avg ', self.clustering_avg

############################################################################

	def get_convert_list_to_mat(self, _list):

		self.adj_mat = np.zeros((_list.shape[0],_list.shape[0]))	
		for i in xrange(0, _list.shape[0]):
		
			for j in xrange(0, _list.shape[1]):

				self.adj_mat[i, _list[i,j]] = 1.0 

############################################################################

	def get_convert_mat_to_list(self,_mat):

		adj = []

		for i in xrange(0,_mat.shape[0]):

			for j in xrange(0, _mat.shape[1]):

				if(_mat[i,j] > 0):
					adj.append((i,j))
		return adj

############################################################################
		
	def get_degrees(self, _mat):

		self.degree_mat = np.asarray([len(np.nonzero(_mat[i,])[0]) for i in xrange(_mat.shape[0])])
	
		self.degree_avg = np.sum(self.degree_mat) / self.degree_mat.shape[0]
			
		self.degree_hist, _ = np.histogram(self.degree_mat)
		
		self.order = self.degree_mat.shape[0]

		if(self.properties['directed'] == 1):
			self.length = np.sum(self.degree_mat)
		else:
			self.length = np.sum(self.degree_mat) /2
		if(np.sum(np.diag(self.degree_mat))> 0):
			self.properties['simple'] = 0

		
############################################################################

	def get_clustering_coef(self, _mat):
		self.clustering_mat = np.zeros((_mat.shape[0]))
		for i in xrange(_mat.shape[0]):
			
			me = np.nonzero(_mat[i,])[0]
			e = 0
			for j in xrange(me.shape[0]):

				neigh = np.nonzero(_mat[me[j],])[0]

				e += np.sum([np.sum(np.equal(neigh[k],me)) for k in xrange(len(neigh))])			
				
			if self.properties['directed'] == 0:
				e /= 2.0
			
			if e > 0:
				self.clustering_mat[i] = 2*e / (self.degree_mat[i]*(self.degree_mat[i]-1))				
			#print i, j, e,self.degree_mat[i], self.clustering_mat[i]
	
		self.clustering_avg = np.sum(self.clustering_mat) / self.clustering_mat.shape[0] 


	
############################################################################

'''
a = np.loadtxt('/home/jeferson/Dropbox/test_graph.txt')

gra = GraphMetric(a)

gra.get_degrees(a)

gra.get_clustering_coef(a)

gra.set_adj_mat(a)

print gra.get_shortest_path()

'''


