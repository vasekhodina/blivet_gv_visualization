import unittest
import sys
sys.path.append("..")
import node

class TestNode(unittest.TestCase):
    def setUp():
        self.node = node.Node("test01", "disk", "ext4", "10 MB", "/some/path")

    def test_name_assignment(self):
        self.assertEqual(node.getAttribute("name"), "test01") 

    def test_prepare(self):
        self.node.prepare()
        self.assertEqual(self.node.getGvAttributes()["label"], "Name: test01\nType: disk\nFormat(FS): ext4\nsize: 10 MB\npath: /some/path"


    def test_change_color(self):
        self.node.change_color("red")
        self.assertEquals(self.node.getGvAttributes()["style"], "filled")
        self.assertEquals(self.node.getGvAttributes()["fillcolor"], "red")

    def test_change_shape(self):
        self.node.change_color("red")
        self.node.change_shape("rounded-box")
        self.assertEquals(node.getGvAttributes()["style"], "filled, rounded")
        

    def test_adding_action(self):
        self.node.addAttribute("action", "first_action")
        self.node.addAttribute("action", "second_action")
        self.assertEquals(self.node.getAttributes()["action"], "first_action second_action")


    def main():
        unittest.main()

if __name__ == '__main__':
    unittest.main()
