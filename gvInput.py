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
				self.processNode(node_to_be_added)
				node_list.append(node_to_be_added)	
				print("Adding device, Name: " + n.name + " Type: " + n.type)
				if n.parents:
					if n.parents[0].type == "luks//dm-crypt":
						edge_to_be_added = edge.Edge(n.parents[0].parents[0].name,n.name)
					else:
						edge_to_be_added = edge.Edge(n.parents[0].name,n.name)
						edge_list.append(edge_to_be_added)

	def processNode(self, node):
		if node.getType() == "luks/dm-crypt":
			self.nodeIsLuks(node)

	def colorNode(self, node, color):
		node.addGvAttribute("style","filled")	
		node.addGvAttribute("fillcolor",color)	

	def reshapeNode(self,shape):
		return

	def nodeIsHarddrive(self):
		return

	def nodeIsLVM(self):
		return

	def nodeIsRAID(self):
		return
	
	def nodeIsLuks(self, node):
		self.colorNode(node, "blue")	
    
	#def getDataFromXML():

