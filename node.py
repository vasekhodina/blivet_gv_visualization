class Node(object):

    def __init__(self, name, disk_type, status="", uuid="", path="", size=""):
        self.__name = name
        self.__disk_type = disk_type
        self.__gv_attributes = {}
        self.__attributes = {}
        self.__label = ""
        if status is not None:
            self.__attributes['status'] = status
        if uuid is not None:
            self.__attributes['uuid'] = uuid
        if path is not None:
            self.__attributes['path'] = path
        if size is not None:
            self.__attributes['size'] = size

    def setName(name):
        self.__name = name

    def setType(disk_type):
        self.__disk_type = disk_type

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

    def change_color(self, color):
        self.change_style("filled")
        self.addGvAttribute("fillcolor", color)

    def change_style(self, style):
        if not self.__gv_attributes["style"]:
            self.addGvAttribute("style", style)
        else:
            self.addGvAttribute("style",
                                self.getGvAttributes()["style"] + ", " + style)
