class Edge(object):
    """ Class containing the variables and functions needed for edges in graph. """

    def __init__(self, node_from, node_to):
        self.__node_from = node_from
        self.__node_to = node_to
        self.gv_attributes = {}

    def getFrom(self):
        return self.__node_from

    def getTo(self):
        return self.__node_to

    def addGvAttribute(self, attr, value):
        """ Adds a graphviz attribute of edge. Any should work.
        :param str attr The name of the attribute that should be added.
        :param str value The value of the attribute."""
        self.gv_attributes[str(attr)] = str(value)
