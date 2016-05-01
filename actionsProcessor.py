import pallete
import node
import gvInput

class ActionsProcessor():
    def __init__(self, actions_list, node_list, edge_list):
        self.actions = actions_list
        self.node_list = node_list
        self.edge_list = edge_list
        self.pallete = pallete.Pallete()
        self.gv_input = gvInput.GvInput(node_list, edge_list)

    def processActions(self):
        print("Actions:")
        for action in self.actions:
            found_node = self.find_node(action.device.name)
            if not found_node:
                found_node = node.Node(action.device.name, action.device.type, action.device.format, action.device.size, action.device.path)
                self.gv_input.processNode(found_node,action.device)
            self.process_action(action, found_node)

    def process_action(self, action, node):
        if action.isDestroy or isRemove:
            node.addAttribute("action", "Delete")
            node.change_color(self.pallete.complement["2"])
        if action.isCreate or action.isAdd:
            node.addAttribute("action", "Add")
            node.change_color(self.pallete.primary["2"])
        if action.isResize or action.isShrink or action.isGrow:
            node.addAttribute("action", "Modify")
            node.change_color(self.pallete.secondary_first["2"])
        if action.isFormat:
            node.addAttribute("action", "Format")
            node.change_color(self.pallete.secondary_first["2"])

    def find_node(self, dev_name):
        print("In find_node")
        for found_node in self.node_list:
            print("Checking: " + found_node.getName() +  " and " + dev_name)
            if found_node.getName() == dev_name: 
                print("Found node: " + found_node.getName())
                return found_node
