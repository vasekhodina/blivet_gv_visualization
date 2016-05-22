from os import path
import graphviz
import xml.etree.ElementTree as ET


class Output:
    """ Class for creating graphs, uses data loaded previously. """

    def __init__(self, node_list, edge_list):
        self.graph = self.create_gv_graph(node_list, edge_list)

    def create_svg(self, graph_abs_path, graph_name):
        """ Creates an SVG file from the graph object that is stored as attribute of Output class.
        :param str graph_name Filename that the graph should have.
        :param str graph_abs_path Absolute path leading to the directory where the graph should be created."""
        svg_string = self.graph.pipe(format="svg").decode(encoding="UTF-8")
        svg_tree = self.insert_JS_to_graph(svg_string)
        print("Full path of graph: " + graph_abs_path + "/" + graph_name + ".svg")
        svg_tree.write(graph_abs_path + "/" + graph_name + ".svg", "utf-8")

    def create_gv_graph(self, node_list, edge_list):
        """ Creates a graph object from list of nodes and list of edges.
        :param list node_list List of nodes the graph should contain, prepared for visualization.
        :param list edge_list List of edges the graph sould contain.
        :return graph The graphviz graph object.
        :rtype object"""
        graph = graphviz.Digraph("degraph")
        for i in node_list:
            new_node = graph.node(str(i.getName()), i.getGvAttributes()["label"],
                                  i.getGvAttributes())
        for i in edge_list:
            if i.gv_attributes is None:
                graph.edge(str(i.getFrom()), str(i.getTo()))
            else:
                graph.edge(str(i.getFrom()), str(i.getTo()), _attributes=i.gv_attributes)
        return graph

    def insert_JS_to_graph(self, graph_string):
        """ Helper function that opens a graph from string as XML and does some modifications to it. Removes unneccesarry element and attributes
        and inputs new ones like links to Javascript files.
        :param str graph_string Graphviz graph object converted to a string.
        :return tree XML element tree object containing svg of the graph
        :rtype xml.etree.ElementTree object"""

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
                if text_subelement.tag == "{http://www.w3.org/2000/svg}text":
                    if pos < 3:
                        text_subelement.set("font-size", "18.00")
                        text_subelement.set("transform", "translate(0, " + str(pos*10) + ")")
                        pos += 1
                    elif pos == 3 and text_subelement.text.find("Format") > -1:
                        text_subelement.set("font-size", "18.00")
                        text_subelement.set("transform", "translate(0, " + str(pos*10) + ")")
                        pos += 1
                    else:
                        text_subelement.set("visibility", "hidden")
                        pos += 1
        return tree
