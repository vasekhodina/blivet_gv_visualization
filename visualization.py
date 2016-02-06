import blivet
import gv
import gvInput

class Visualization(object):
	
	def createGraph(self,graph_name):
		node_list = []
		edge_list = []
		gv_input = gvInput.GvInput()
		gv_input.getDataFromBlivet(node_list, edge_list)
		output = output.Output()
		output.createSvg()
		output.createGtk()



