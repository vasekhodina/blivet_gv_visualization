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
		#blacklist of devices that should not be displayed in a graph, i.e. cdrom
		blacklist = ["cdrom"]
		for n in blvt.devices:
			if not n.type in blacklist:
				node_to_be_added = node.Node(n.name,n.type,n.size)
				node_list.append(node_to_be_added)	
				print "Adding " + n.name + " " + n.type# + " " +  n.size
			else:
				break
			if n.parents:
				print " " + n.parents[0].name
				if n.parents[0].type == "luks/dm-crypt":
					edge_to_be_added = edge.Edge(n.parents[0].parents[0].name,n.name)
				else:
					edge_to_be_added = edge.Edge(n.parents[0].name,n.name)
					edge_list.append(edge_to_be_added)

		graph = gv.digraph("Graph")
		for i in node_list:
			gv.node(graph,str(i.getName()))
		for i in edge_list:
			gv.edge(graph,str(i.getFrom()),str(i.getTo()))	
		gv.layout(graph,"dot")
		gv.render(graph,"svg",str(graph_name))




