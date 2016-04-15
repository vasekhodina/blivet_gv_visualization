import blivet.blivet
import node
import edge
import pallete


class GvInput:

    def __init__(self, node_list, edge_list, blvt = ""):
        self.pallete = pallete.Pallete()
        self.node_list = node_list
        self.edge_list = edge_list
    def getDataFromBlivet(self):
        blacklist = ["cdrom"]
        if blvt == "":
            blvt = blivet.Blivet()
            blvt.reset()
        for n in blvt.devices:
            if n.type not in blacklist:
                node_to_be_added = node.Node(n.name, n.type, n.format, n.size, n.path, n.uuid)
                self.processNode(node_to_be_added,n)
                self.node_list.append(node_to_be_added)
                print("Adding device, Name: " + n.name + " Type: " + n.type)
                for parent in n.parents:
                    if parent.type == "luks//dm-crypt":
                        edge_to_be_added = edge.Edge(parent.parents[0].name, n.name)
                    else:
                        edge_to_be_added = edge.Edge(parent.name, n.name)
                        self.edge_list.append(edge_to_be_added)

    def processNode(self, node, device):
        if node.getType() == "luks/dm-crypt":
            self.nodeIsLuks(node)
        if node.getType() == "disk":
            self.nodeIsHarddrive(node)
            if (node.format.type == "disklabel"):
                node.addAttribute("format", node.format.labelType)
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
            self.nodeIsLVMSnapshot()
            edge = edge.Edge(node.getName(), device.origin.name)
            self.edge_list.append(edge)

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

    def nodeIsMDRAID():
        node.change_color(self.pallete.secondary_first["0"])
        node.change_shape("octagon")

    def nodeIsLVMSnapshot():
        node.change_color(self.pallete.secondaty_first["3"])
        node.change_shape("rounded-box")

    # def getDataFromXML():
