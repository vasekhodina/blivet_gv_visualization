import gv

class Output:
    def createSvgFromGraph(graph,graph_name):
        gv.render(graph,"svg",str(graph_name)
