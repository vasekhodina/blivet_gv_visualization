# TODO add these two lines to the svg programatically:
# <script xlink:href="SVGPan.js"/>
# <g id="viewport" transform="translate(200,200)">
# and delete everything except xmlns width and height tags in <svg>
import graphviz


class Output:
    def __init__(self, node_list, edge_list):
        self.graph = self.createGvGraph(node_list, edge_list)

    def createSvg(self, graph_name):
        svg_file = open(graph_name, "w")
        svg_file.write(self.graph.pipe(format="svg").decode(encoding="UTF-8"))
        svg_file.close()

    def createGvGraph(self, node_list, edge_list):
        graph = graphviz.Digraph("degraph")
        for i in node_list:
            new_node = graph.node(str(i.getName()), i.getGvAttributes()["label"],
                                  i.getGvAttributes())
        for i in edge_list:
            graph.edge(str(i.getFrom()), str(i.getTo()))
        return graph
