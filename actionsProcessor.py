import pallete

class ActionProcessor():
    def __init__(self, actions_list, node_list, edge_list):
        self.actions = actions_list
        self.node_list = node_list
        self.edge_list = edge_list

    def processActions(self):
        for action in actions:
            node = self.find_node(action.dev.name)
            process_action(action, node)

    def processAction(self, action, node):
        if action.isDestroy() or isRemove():
            node.addAttribute("action", "Delete")
        if action.isCreate() or action.isAdd():
            node.addAttribute("action", "Add")
        if action.isResize() or action.isShrink() or action.isGrow:
            node.addAttribute("action", "Modify")
        if action.isFormat():
            node.addAttribute("action", "Format")
