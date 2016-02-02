import blivet
import gv

class Visualization(object):
	
	def createGraph(self,graph_name):
		node_list = []
		edge_list = []
                gv_input = gvInput.GvInput()
                gvInput.getDataFromBlivet(node_list, edge_list)
                output = output.Output()
                output.createSvg()




