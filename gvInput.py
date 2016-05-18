import emoji

import blivet.blivet
import node
import edge
import pallete


class GvInput:
    """ Class for loading data from blivet """

    def __init__(self, node_list, edge_list, path_to_pallete, blvt=None): 
        self.pallete = pallete.Pallete(path_to_pallete)
        self.node_list = node_list
        self.edge_list = edge_list
        if blvt is None:
            self.blvt = blivet.Blivet()
            self.blvt.reset()
        else:
            self.blvt = blvt

    def getDataFromBlivet(self):
        """ Function that loads data from blivet. Uses attributes of GvInput object."""
        blacklist = ["cdrom"]
        for n in self.blvt.devices:
            if n.type not in blacklist:
                node_to_be_added = node.Node(n.name, n.type, n.format.type, n.size, n.path, n.uuid)
                self.processNode(node_to_be_added,n)

    def processNode(self, node, device):
        """ Sorts node based on it's type and starts command related to it.
        :param obj node node that should be sorted
        :param obj device the device from which the node originated, used for getting aditional information"""
        print("Adding device, Name: " + device.name + " Type: " + device.type)
        # Adding entries that are present for all nodes
        if (device.encrypted):
            node.add_emoji(emoji.emojize(":lock:"))
        else:
            node.add_emoji(emoji.emojize(":open_lock:"))
        # End of common entries
        if node.getType() == "luks/dm-crypt":
            self.nodeIsLuks(node)
        if node.getType() == "disk":
            self.nodeIsHarddrive(node)
            if (device.format.type == "disklabel"):
                node.addAttribute("format", device.format.labelType)
        if node.getType() == "partition":
            self.nodeIsPartition(node)
        if node.getType() == "lvmlv":
            self.nodeIsLV(node)
            if (device.cached):
                node.addAttribute("cached", "True")
        if node.getType() == "lvmvg":
            self.nodeIsVG(node)
        if node.getType() == "lvmthinpool":
            self.nodeIsLVMThinPool(node)
        if node.getType() == "lvmthinlv":
            self.nodeIsLVMThinLv(node)
            if (device.cached):
                node.addAttribute("cached", "True")
        if node.getType() == "btrfs volume":
            self.nodeIsBTRFS(node)
        if node.getType() == "mdarray":
            self.nodeIsMDRAID(node) 
        if node.getType() == "lvmsnapshot":
            self.nodeIsLVMSnapshot(node)
            new_edge = edge.Edge(device.origin.name, node.getName())
            new_edge.addGvAttribute("style", "dashed")
            self.edge_list.append(new_edge)
        self.node_list.append(node)
        for parent in device.parents:
            edge_to_be_added = edge.Edge(parent.name, device.name)
            self.edge_list.append(edge_to_be_added)

    def nodeIsHarddrive(self, node):
        node.change_shape("Msquare")
        node.change_color(self.pallete.secondary_first["4"])

    def nodeIsPartition(self, node):
        node.change_shape("box")
        node.change_color(self.pallete.secondary_first["2"])

    def nodeIsLV(self, node):
        node.change_shape("rounded-box")
        node.change_color(self.pallete.secondary_first["2"])

    def nodeIsVG(self, node):
        node.change_color(self.pallete.secondary_first["3"])

    def nodeIsLuks(self, node):
        node.change_color(self.pallete.secondary_first["0"])

    def nodeIsBTRFS(self, node):
        node.change_shape("hexagon")
        node.change_color(self.pallete.secondary_first["2"])

    def nodeIsLVMThinPool(self, node):
        node.change_color(self.pallete.secondary_first["1"])

    def nodeIsLVMThinLv(self,node):
        node.change_shape("rounded-box")
        node.change_color(self.pallete.secondary_first["1"]) 

    def nodeIsMDRAID(self,node):
        node.change_color(self.pallete.secondary_first["0"])
        node.change_shape("octagon")

    def nodeIsLVMSnapshot(self,node):
        node.change_color(self.pallete.secondary_first["3"])
        node.change_shape("rounded-box")

    # def getDataFromXML():
