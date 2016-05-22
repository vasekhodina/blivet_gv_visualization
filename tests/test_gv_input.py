import unittest
import sys
#from blivet_gv_visualization import gvInput
sys.path.append("./..")
import gvInput

class TestGvInput(unittest.TestCase):
    def setUp(self):
        self.node_list = []
        self.edge_list = []
        self.gvInput = gvInput.GvInput(self.node_list, self.edge_list, "./../assets/pallete.xml")

    def test_blivet_init(self):
        self.assertIsNotNone(self.gvInput.blvt)

    def test_get_data_from_blivet(self):
        self.gvInput.get_data_from_blivet()
        self.assertIsNotNone(self.node_list[0])

    def test_process_node(self):
        self.gvInput.get_data_from_blivet()
        for n in self.node_list:
            if n.getType() == "disk":
                self.assertEqual(n.getGvAttributes()["shape"], "Msquare")

if __name__ == '__main__':
    unittest.main()
