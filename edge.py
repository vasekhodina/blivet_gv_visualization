class Edge(object):
	def __init__(self,node_from,node_to):
		self.__node_from=node_from
		self.__node_to=node_to
	def getFrom(self):
		return self.__node_from
	def getTo(self):
		return self.__node_to
