import xml.etree.ElementTree as ET

class Pallete:
    def __init__(self):
        tree = ET.parse("pallete.xml")
        root = tree.getroot()
        self.primary = self.fill_colorset("primary")
        self.secondary_first = self.fill_colorset("secondary-1")
        self.secondary_second = self.fill_colorset("secondary-2")
        self.complement = self.fill_colorset("complement")

    def fill_colorset(self, id):
        colorset = {}
        colorset_element = root.find("colorset{id='" + id + "'")
        for color in colorset_element.iter():
            colorset[color.get("nr")] = "#" + color.get("rgb")
        return colorset

p = Pallete()
print(p.primary)
print(p.secondary_first)
print(p.secondary_second)
print(p.complement)
