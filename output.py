from os import path
import graphviz
import xml.etree.ElementTree as ET


class Output:
    def __init__(self, node_list, edge_list):
        self.graph = self.createGvGraph(node_list, edge_list)

    def createSvg(self, graph_name, graph_abs_path):
        svg_string = self.graph.pipe(format="svg").decode(encoding="UTF-8")
        svg_tree = self.insert_JS_to_graph(svg_string)
        svg_tree.write(graph_abs_path + "/" + graph_name + ".svg", "utf-8")

    def createGvGraph(self, node_list, edge_list):
        graph = graphviz.Digraph("degraph")
        for i in node_list:
            new_node = graph.node(str(i.getName()), i.getGvAttributes()["label"],
                                  i.getGvAttributes())
        for i in edge_list:
            graph.edge(str(i.getFrom()), str(i.getTo()))
        return graph

    def insert_JS_to_graph(self, graph_string):
        # Load svg as XML
        ET.register_namespace("", "http://www.w3.org/2000/svg")
        tree = ET.ElementTree(ET.fromstring(graph_string))
        root = tree.getroot()
        # Deal with root (<svg> element) attributes
        root.set("xmlns:xlink", "http://www.w3.org/1999/xlink")
        del root.attrib["viewBox"]
        # Prepare first child for JS
        graph_element = root.find("./*[@id='graph0']")
        graph_element.set("id", "viewport")
        # Add the scripts
        new_element = ET.Element("script")
        new_element.set("xlink:href", path.abspath("./JS") + "/SVGPan.js")
        root.insert(0,new_element)
        new_element = ET.Element("script")
        new_element.set("xlink:href", path.abspath("./JS") + "/vis_util.js")
        root.insert(0,new_element)

        node_elements = root.findall(".//*[@class='node']")
        for element in node_elements:
            element.set("onclick","zoomNode(this)")
            pos = 0
            for text_subelement in element:
                print(text_subelement.tag)
                if text_subelement.tag == "{http://www.w3.org/2000/svg}text":
                    if pos < 3:
                        text_subelement.set("font-size", "18.00")
                        text_subelement.set("transform", "translate(0, " + str(pos*10) + ")")
                        pos += 1
                    else:
                        text_subelement.set("visibility", "hidden")
                        pos += 1
        return tree
