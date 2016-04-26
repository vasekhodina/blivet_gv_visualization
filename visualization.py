import os

import gvInput
import output


class Visualization(object):
    """Main class of the program, holds the important data (node and edge lists)."""

    def __init__(self):
        self.node_list = []
        self.edge_list = []

    def prepareNodes(self):
        """ prepare the nodes in node_list
        :param self"""
        for n in self.node_list:
            n.prepare()

    def createGraph(self, graph_name, graph_abs_path):
        """ Function that creates the a visualized graph using data extracted from blivet
        :param self
        :param str graph_name filename of the graph that is being created
        :param graph_abs_path absolute path to the directory where the graph should be created"""
        if not os.path.exists(graph_abs_path):
            os.mkdir(graph_abs_path)  
        gv_input = gvInput.GvInput(self.node_list, self.edge_list)
        gv_input.getDataFromBlivet()
        self.prepareNodes()
        out = output.Output(self.node_list, self.edge_list)
        out.createSvg(graph_name, graph_abs_path)

