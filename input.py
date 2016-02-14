import blivet.blivet
#TODO nodes sorting, need to add parent into graph node and put nodes without parents into graph first
class Input:
    def getDataFromBlivet(node_list, edge_list):
        blacklist = ["cdrom"]
        blvt = blivet.Blivet()
        blvt.reset()
	for n in blvt.devices:
       	if not n.type in blacklist:
			node_to_be_added = node.Node(n.name,n.type,n.size)
			node_list.append(node_to_be_added)	
			print "Adding " + n.name + " " + n.type# + " " +  n.size
			if n.parents:
				print "First parent: " + n.parents[0].name 
				if n.parents[0].type == "luks/dm-crypt":
					print "Second parent: " + n.parents[0].parents[0].name
					edge_to_be_added = edge.Edge(n.parents[0].parents[0].name,n.name)
				else:
					edge_to_be_added = edge.Edge(n.parents[0].name,n.name)
					edge_list.append(edge_to_be_added)
    
    def getDataFromXML():

