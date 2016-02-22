import blivet.blivet
import gv
import gvInput
import output

class Visualization(object):
	def prepareNodes(self,node_list):
		for n in node_list:
			n.prepare()
	
	def createGraph(self,graph_name):
		node_list = []
		edge_list = []
		gv_input = gvInput.GvInput()
		gv_input.getDataFromBlivet(node_list, edge_list)
		self.prepareNodes(node_list)
		out = output.Output(node_list, edge_list)
		out.createSvg(graph_name)
		#out.createGtk(graph_name)


