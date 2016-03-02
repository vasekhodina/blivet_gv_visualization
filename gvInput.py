import blivet.blivet
import node
import edge
class GvInput:
	def getDataFromBlivet(self,node_list, edge_list):
		blacklist = ["cdrom"]
		blvt = blivet.Blivet()
		blvt.reset()
		for n in blvt.devices:
			if not n.type in blacklist:
				node_to_be_added = node.Node(n.name,n.type,n.status,n.uuid,n.path,n.size)
				self.colorNode(n,node_to_be_added)
				node_list.append(node_to_be_added)	
				if n.parents:
					if n.parents[0].type == "luks//dm-crypt":
						edge_to_be_added = edge.Edge(n.parents[0].parents[0].name,n.name)
					else:
						edge_to_be_added = edge.Edge(n.parents[0].name,n.name)
						edge_list.append(edge_to_be_added)

	def colorNode(self, device, node):
		if device.type == "luks/dm-crypt":
			node.addGvAttribute("fillcolor","blue")	
			node.addGvAttribute("style","filled")	
			
    
	#def getDataFromXML():
