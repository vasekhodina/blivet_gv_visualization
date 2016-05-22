import unittest
import sys
sys.path.append("./..")

import output
import gvInput
import xml.etree.ElementTree as ET

class TestOutput(unittest.TestCase):
    def setUp(self):
        self.node_list = []
        self.edge_list = []
        self.gv_input = gvInput.GvInput(self.node_list, self.edge_list, "../assets/pallete.xml")
        self.gv_input.get_data_from_blivet()
        for n in self.node_list:
            n.prepare()
        self.output = output.Output(self.node_list, self.edge_list)

    def test_insert_JS_to_graph(self):
        tree = self.output.insert_JS_to_graph(self.output.graph.pipe(format="svg").decode(encoding="UTF-8"))
        root = tree.getroot()
        self.assertIsNone(root.attrib.get("viewBox"))

if __name__ == '__main__':
    unittest.main()
