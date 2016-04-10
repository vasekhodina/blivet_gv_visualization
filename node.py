class Node(object):

    def __init__(self, name, disk_type, format="", size="", path="", uuid=""):
        self.__name = name
        self.__disk_type = disk_type
        self.__gv_attributes = {}
        self.__attributes = {}
        self.__label = ""
        if format is not None:
            addAttribute('format', format)
        if size is not None:
            addAttribute('size', size)
        if path is not None:
            addAttribute('path', path )
        if uuid is not None:
            addAttribute('uuid', uuid )

    def setName(name):
        self.__name = name

    def setType(disk_type):
        self.__disk_type = disk_type

    def addAttribute(attribute_name, value)
        self._attributes[attribute_name] = value

    def addGvAttribute(self, attr, value):
        self.__gv_attributes[str(attr)] = str(value)

    def getName(self):
        return self.__name

    def getType(self):
        return self.__disk_type

    def getGvAttributes(self):
        return self.__gv_attributes

    def prepare(self):
        self.__label = "Name: " + self.__name + "\n" + "Type: " + self.__disk_type + "\n"
        for k, v in self.__attributes.items():
            self.__label = self.__label + str(k) + ": " + str(v) + "\n"
        self.addGvAttribute("label", self.__label)
        self.addGvAttribute("comment","comment")

    def change_color(self, color):
        self.change_style_safely("filled")
        self.addGvAttribute("fillcolor", color)

    def change_shape(self, shape):
        if shape == "rounded-box":
            self.change_shape("box")
            self.change_style_safely("rounded")
        else:
            self.addGvAttribute("shape",shape)

    def change_style_safely(self, style):
        if self.__gv_attributes.get("style", None) is None:
            self.addGvAttribute("style", style)
        else:
            oldstyle = self.getGvAttributes()["style"]
            del self.__gv_attributes["style"]
            self.addGvAttribute("style", oldstyle + ", " + style) 
            print(oldstyle)
