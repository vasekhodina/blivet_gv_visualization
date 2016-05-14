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
        self.gv_input.getDataFromBlivet()
        self.output = output.Output(node_list, edge_list)

    def test_insert_JS_to_graph(self):
        tree = self.output.insert_JS_to_graph(self.output.graph.pipe(format="svg").decode(encoding="UTF-8")
        root = tree.getroot()
        self.assertIsNone(root.attrib["viewBox"])
        graph_el = root.find("./*[@id='graph0']")
        self.assertEqual(graph_el.attrib["id"], "viewport")
        script_list = root.findall("script")
        self.assertEqual(len(script_list), 2)

        

if __name__ == '__main__':
    unittest.main()
