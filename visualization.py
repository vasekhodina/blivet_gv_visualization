import blivet
import gv
import node
import edge

class Visualization(object):
	
	def createGraph(self,graph_name):
		blvt = blivet.Blivet()
		blvt.reset()

		node_list = []
		edge_list = []
		for n in blvt.devices:
			node_to_be_added = node.Node(n.name,n.type,n.size)
			node_list.append(node_to_be_added)	
			if n.parents:
				edge_to_be_added = edge.Edge(n.parents[0].name,n.name)
				edge_list.append(edge_to_be_added)

		graph = gv.digraph("Graph")
		for i in node_list:
			gv.node(graph,str(i.getName()))
		for i in edge_list:
			gv.edge(graph,str(i.getFrom()),str(i.getTo()))	
		gv.layout(graph,"dot")
		gv.render(graph,"svg",str(graph_name))




