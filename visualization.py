import os

import gvInput
import output
import actionsProcessor


class Visualization(object):
    """Main class of the program, holds the important data (node and edge lists)."""
    def __init__(self, blivet=""):
        self.blivet = blivet
        print(self.blivet)
        self.node_list = []
        self.edge_list = []

    def prepareNodes(self):
        """ prepare the nodes in node_list """
        for n in self.node_list:
            n.prepare()

    def createGraph(self, graph_name, graph_abs_path):
        """ Function that creates the a visualized graph using data extracted from blivet
        :param str graph_name filename of the graph that is being created
        :param graph_abs_path absolute path to the directory where the graph should be created
        :param object blivet Blivet object from which to take the data
        """
        if not os.path.exists(graph_abs_path):
            os.mkdir(graph_abs_path)  
        gv_input = gvInput.GvInput(self.node_list, self.edge_list, self.blivet)
        gv_input.getDataFromBlivet()
        self.prepareNodes()
        out = output.Output(self.node_list, self.edge_list)
        out.createSvg(graph_name, graph_abs_path)

    def create_actions_graph(self, graph_name, graph_abs_path):
        """ Function that creates the a visualized graph using data extracted from blivet
        :param str graph_name filename of the graph that is being created
        :param graph_abs_path absolute path to the directory where the graph should be created
        :param object blivet Blivet object from which to take the data
        """
        if not os.path.exists(graph_abs_path):
            os.mkdir(graph_abs_path)  
        gv_input = gvInput.GvInput(self.node_list, self.edge_list, self.blivet)
        gv_input.getDataFromBlivet()
        print(self.blivet.devicetree.actions.find())
        actions_processor = actionsProcessor.ActionsProcessor(self.blivet.devicetree.actions.find(), self.node_list, self.edge_list)
        actions_processor.processActions()
        self.prepareNodes()
        out = output.Output(self.node_list, self.edge_list)
        out.createSvg(graph_name, graph_abs_path)
