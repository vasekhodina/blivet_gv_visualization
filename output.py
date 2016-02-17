import gv

class Output:

	def __init__(self, node_list, edge_list):
		self.graph=self.createGvGraph(node_list, edge_list)

	def createSvg(self,graph_name):
		gv.layout(self.graph,"dot")
		gv.render(self.graph,"svg",str(graph_name))
	
	def createGtk(self,graph_name):
		gv.layout(self.graph,"dot")
		gv.render(self.graph,"tk",str(graph_name))

	def createGvGraph(self,node_list, edge_list):
		graph = gv.digraph("degraph")
		for i in node_list:
			new_node = gv.node(graph,str(i.getName()))
			print i.getLabel()
			gv.setv(new_node,"label",str(i.getLabel()))
		for i in edge_list:
			gv.edge(graph,str(i.getFrom()),str(i.getTo()))	
		return graph
