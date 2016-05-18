class Node(object):
    """ Class holding all the variables for nodes that should be displayed in a graph. 
    also contains neccessary helper functions """

    def __init__(self, name, disk_type, format="", size="", path="", uuid=""):
        self.__name = name
        self.__disk_type = disk_type
        self.__gv_attributes = {}
        self.__attributes = {}
        self.__label = ""
        self.emojis = ""
        if format is not None:
            self.addAttribute('format', format)
        if size is not None:
            self.addAttribute('size', size)
        if path is not None:
            self.addAttribute('path', path )
        if uuid is not None or not uuid == "None" or not uuid == "\n" or not uuid == "":
            self.addAttribute('uuid', uuid )

    def setName(self,name):
        self.__name = name

    def setType(self,disk_type):
        self.__disk_type = disk_type

    def addAttribute(self, attribute_name, value):
        """ Function that serves to ease the task of setting attributes of node. Do not confuse with set_gv_attributes,
        which sets graphviz visualization attributes. 
        :param str attribute_name name of the attribute
        :param value the value of the attribute that should be set up"""
        if attribute_name == "action" and self.__attributes.get("action", None) is not None:
            old_action = self.__attributes["action"]
            del self.__attributes["action"]
            self.addAttribute("action", old_action +  " " + str(value))
        else:
            self.__attributes[str(attribute_name)] = str(value)

    def addGvAttribute(self, attr, value):
        """ Function that serves to ease the task of setting visualization attributes of node. Do not confuse with 
        set_attributes, which sets general information attributes. 
        :param str attribute_name name of the attribute
        :param value the value of the attribute that should be set up"""
        self.__gv_attributes[str(attr)] = str(value)

    def add_emoji(self, value):
        """ Function that serves to ease the task of setting attributes of node. Serves only for setting attributes you
        do not want visible anywhere.
        :param str value The value of the attribute that should be set up."""
        self.emojis = self.emojis + value

    def getName(self):
        return self.__name

    def getType(self):
        return self.__disk_type

    def getGvAttributes(self):
        return self.__gv_attributes

    def getAttributes(self):
        return self.__attributes

    def prepare(self):
        """ Prepares the node for visualization, ie. puts all the attributes into node label so they are visible in the graph."""
        if not self.emojis == "":
            self.__label = self.emojis + "\n"
        self.__label = self.__label + "Name: " + self.__name + "\nType: " + self.__disk_type + "\nFormat(FS): " + str(self.__attributes.pop("format",{"format" : "None"}))
        for k, v in self.__attributes.items():
            self.__label = self.__label + "\n" + str(k) + ": " + str(v)
        self.addGvAttribute("label", self.__label)

    def change_color(self, color):
        """ Function serving for setting and changing color. Set' up additional graphviz attributes so colorchange is visible
        :param str color Any color value that is accepted by the output engine you are going to use."""
        self.change_style_safely("filled")
        self.addGvAttribute("fillcolor", color)

    def change_shape(self, shape):
        """ This function serves for changing of node shapes. Normally uses graphviz shapes but has additional shapes on its own like rounded-box. A box shape
        with round corners.
        :param str shape The desired shape the node shoul have."""
        if shape == "rounded-box":
            self.change_shape("box")
            self.change_style_safely("rounded")
        else:
            self.addGvAttribute("shape",shape)

    def change_style_safely(self, style):
        """ Helper function for function change shape, but can serve as style changer on it's own.
        :param str style The desired style of the node."""
        if self.__gv_attributes.get("style", None) is None:
            self.addGvAttribute("style", style)
        else:
            oldstyle = self.getGvAttributes()["style"]
            del self.__gv_attributes["style"]
            self.addGvAttribute("style", oldstyle + ", " + style) 
