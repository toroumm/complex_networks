import igraph
import numpy as np

#shapes
#"circle"     "square"     "csquare"    "rectangle"  "crectangle"

class BuildGraph:

	def __init__(self):

		self._graph = igraph.Graph(directed = True)

		self.visual_style = {}

		self.set_style()

		self.typeNode  = {'package':{'arrow_size': None, 'color': 'green', 'label': None, 'shape':
 'rectangle', 'asp': None, 'margin': None, 'size': 120}, 'class':{'arrow_size': None, 'color': 'red', 'label': None, 'shape':'circle', 'asp': None, 'margin': None, 'size': 140}, 'method':{} }

#**********************************************************************************
	def set_style(self):

		self.visual_style["bbox"] = (5000, 2000)
		self.visual_style["margin"] = 80
		self.visual_style['hovermode'] = 'closest'
		#self.visual_style['layout'] = 'large'		


#**********************************************************************************
	def add_attribute_to_node(self, name, attr,attr_name):

		try:
			v = self._graph.vs.find(name)
		except:

			print ' Atributo', name, attr_name, attr
			sys.exit()		
		try:
			self._graph.vs[v.index][attr_name].append(attr)
		except:
			self._graph.vs[v.index][attr_name] = [attr]

#**********************************************************************************
	def add_node(self, _type, name):

		try:
			if name not in self._graph.vs['label'] or name not in self._graph.vs['Name']:

				self._graph.add_vertex(name)

				v = self._graph.vs.find(name)
				
				for key in self.typeNode[_type].keys():
					self._graph.vs[v.index][key] = self.typeNode[_type][key]
				
				self._graph.vs[v.index]['label'] = name
				self._graph.vs[v.index]['Name'] = name
				self._graph.vs[v.index]['type'] = _type				
		except:

			self._graph.add_vertex(name)

			v = self._graph.vs.find(name)

			for key in self.typeNode[_type].keys():
				self._graph.vs[v.index][key] = self.typeNode[_type][key]

			self._graph.vs[v.index]['label'] = name
			self._graph.vs[v.index]['Name'] = name
			self._graph.vs[v.index]['type'] = _type	

			#self._graph.vs[v.index]['asp'] = 0

#**********************************************************************************				
	def add_edge(self, node_name1, node_name2):

		v1 = self._graph.vs.find(node_name1)

		v2 = self._graph.vs.find(node_name2)

		self._graph.add_edge(v1,v2)

		#get vertex ID
		#es1 = self._graph.es.select(v1,v2)

#**********************************************************************************




#**********************************************************************************
	def plot(self):
		try:
			igraph.plot(self._graph, **self.visual_style)
			#igraph.plot(self._graph, labels = True, **self.visual_style)
		except:
			print 'Problema no PLOT'
			sys.exit()

#################################################################################

