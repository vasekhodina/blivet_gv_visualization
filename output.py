import gv

class Output:
    def createSvg(graph, node_list, edge_list, graph_name):
	for i in node_list:
		gv.node(graph,str(i.getName()))
	for i in edge_list:
		gv.edge(graph,str(i.getFrom()),str(i.getTo()))	
	gv.layout(graph,"dot")
	gv.render(graph,"svg",str(graph_name))
