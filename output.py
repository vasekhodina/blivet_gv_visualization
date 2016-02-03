import gv

class Output:

	def __init__(self, node_list, edge_list):
		self.graph=self.createGvGraph(node_list, edge_list)

    def createSvg(graph_name):
	gv.layout(self.graph,"dot")
	gv.render(self.graph,"svg",str(graph_name))
	
	def createGtk(graph_name):
	gv.layout(self.graph,"dot")
	gv.render(self.graph,"gtk",str(graph_name))

	def createGvGraph(node_list, edge_list)
		graph = gv.digraph()
		for i in node_list:
			gv.node(self.graph,str(i.getName()))
		for i in edge_list:
			gv.edge(self.graph,str(i.getFrom()),str(i.getTo()))	
		return graph
