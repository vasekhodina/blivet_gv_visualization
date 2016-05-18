import unittest
import sys
sys.path.append("..")
import node

class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = node.Node("test01", "disk", "ext4", "10 MB", "/some/path")

    def test_name_assignment(self):
        self.assertEqual(self.node.getName(), "test01") 

    def test_change_color(self):
        self.node.change_color("red")
        self.assertEqual(self.node.getGvAttributes()["style"], "filled")
        self.assertEqual(self.node.getGvAttributes()["fillcolor"], "red")

    def test_change_shape(self):
        self.node.change_color("red")
        self.node.change_shape("rounded-box")
        self.assertEqual(self.node.getGvAttributes()["style"], "filled, rounded")

    def test_adding_action(self):
        self.node.addAttribute("action", "first_action")
        self.node.addAttribute("action", "second_action")
        self.assertEqual(self.node.getAttributes()["action"], "first_action second_action")

if __name__ == '__main__':
    unittest.main()
