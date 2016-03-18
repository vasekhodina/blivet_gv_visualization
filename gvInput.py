import blivet.blivet
import node
import edge


class GvInput:
    def getDataFromBlivet(self, node_list, edge_list):
        blacklist = ["cdrom"]
        blvt = blivet.Blivet()
        blvt.reset()
        for n in blvt.devices:
            if n.type not in blacklist:
                node_to_be_added = node.Node(n.name, n.type, n.status, n.uuid, n.path, n.size)
                self.processNode(node_to_be_added)
                node_list.append(node_to_be_added)
                print("Adding device, Name: " + n.name + " Type: " + n.type)
                if n.parents:
                    if n.parents[0].type == "luks//dm-crypt":
                        edge_to_be_added = edge.Edge(n.parents[0].parents[0].name, n.name)
                    else:
                        edge_to_be_added = edge.Edge(n.parents[0].name, n.name)
                        edge_list.append(edge_to_be_added)

    def processNode(self, node):
        if node.getType() == "luks/dm-crypt":
            self.nodeIsLuks(node)
        if node.getType() == "disk":
            self.nodeIsHarddrive(node)
        if node.getType() == "partition":
            self.nodeIsPartition(node)
        if node.getType() == "lvmlv":
            self.nodeIsLV(node)
        if node.getType() == "lvmvg":
            self.nodeIsVG(node)
        if node.getType() == "lvmthinpool":
            self.nodeIsLVMThinPool(node)
        if node.getType() == "lvmthinlv":
            self.nodeIsLVMThinLv(node)
        if node.getType() == "btrfs volume":
            self.nodeIsBTRFS(node)

    def nodeIsHarddrive(self, node):
        node.change_shape("Msquare")
        node.change_color("lightgreen")

    def nodeIsPartition(self, node):
        node.change_shape("box")
        node.change_color("lightgreen")

    def nodeIsLV(self, node):
        node.change_shape("rounded-box")
        node.change_color("turquoise")

    def nodeIsVG(self, node):
        node.change_color("lightblue")

    def nodeIsRAID(self):
        return

    def nodeIsLuks(self, node):
        node.change_color("lightskyblue")

    def nodeIsBTRFS(self, node):
        node.change_shape("hexagon")
        node.change_color("turquoise")

    def nodeIsLVMThinPool(self, node):
        node.change_color("blueviolet")

    def nodeIsLVMThinLv(self,node):
        node.change_shape("rounded-box")
        node.change_color("darkorchid") 

    # def getDataFromXML():
