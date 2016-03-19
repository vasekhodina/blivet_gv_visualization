import os

import gvInput
import output


class Visualization(object):

    def __init__(self):
        self.node_list = []
        self.edge_list = []

    def prepareNodes(self):
        for n in self.node_list:
            n.prepare()

    def createGraph(self, graph_name, graph_abs_path):
        if not os.path.exists(graph_abs_path):
            os.mkdir(graph_abs_path, mode="0700")
        gv_input = gvInput.GvInput()
        gv_input.getDataFromBlivet(self.node_list, self.edge_list)
        self.prepareNodes()
        out = output.Output(self.node_list, self.edge_list)
        out.createSvg(graph_name, graph_abs_path)

