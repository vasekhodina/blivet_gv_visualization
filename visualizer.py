import os

import gvInput
import output
import actionsProcessor


class Visualizer(object):
    """Main class of the program, holds the important data (node and edge lists)."""
    def __init__(self, blivet=None, palletePath="assets/pallete.xml"):
        self.blivet = blivet
        self.node_list = []
        self.edge_list = []
        self.palletePath = palletePath

    def prepare_nodes(self):
        """ prepare the nodes in node_list """
        for n in self.node_list:
            n.prepare()

    def create_graph(self, graph_abs_path, graph_name):
        """ Function that creates the a visualized graph using data extracted from blivet
        :param str graph_name filename of the graph that is being created
        :param graph_abs_path absolute path to the directory where the graph should be created
        :param object blivet Blivet object from which to take the data
        """
        if not os.path.exists(graph_abs_path):
            os.mkdir(graph_abs_path)  
        gv_input = gvInput.GvInput(self.node_list, self.edge_list, self.palletePath, self.blivet)
        gv_input.get_data_from_blivet()
        self.prepare_nodes()
        out = output.Output(self.node_list, self.edge_list)
        out.create_svg(graph_abs_path, graph_name)

    def create_actions_graph(self, graph_abs_path, graph_name):
        """ Function that creates the a visualized graph using data extracted from blivet
        :param str graph_name filename of the graph that is being created
        :param graph_abs_path absolute path to the directory where the graph should be created
        :param object blivet Blivet object from which to take the data
        """
        if not os.path.exists(graph_abs_path):
            os.mkdir(graph_abs_path)  
        gv_input = gvInput.GvInput(self.node_list, self.edge_list, self.palletePath, self.blivet)
        gv_input.get_data_from_blivet()
        print(self.blivet.devicetree.actions.find())
        actions_processor = actionsProcessor.ActionsProcessor(self.blivet.devicetree.actions.find(), self.node_list, self.edge_list, self.palletePath)
        actions_processor.process_actions()
        self.prepare_nodes()
        out = output.Output(self.node_list, self.edge_list)
        out.create_svg(graph_abs_path, graph_name)
