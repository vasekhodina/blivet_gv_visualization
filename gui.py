import visualizer
import sys
import getopt
from os import path

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Rsvg', '2.0')
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, Rsvg, GdkPixbuf, WebKit


class Gui(Gtk.Window):
    """ Main application window class"""
    def __init__(self, dirname, graph_name):
        self.HEIGHT = 600
        self.WIDTH = 800
        self.dirname = dirname
        self.graph_name = graph_name
        # Init window
        Gtk.Window.__init__(self, title="Disk data visualization")
        self.set_default_size(self.WIDTH, self.HEIGHT)
        # Header Bar
        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.props.title = "Disk data visualization"
        self.set_titlebar(self.hb)
        # Scroll
        self.scroll = Gtk.ScrolledWindow(None, None)
        # Webview
        self.webview = WebKit.WebView()
        self.webview.set_size_request(self.WIDTH - 50, self.HEIGHT - 80)
        # Button
        self.button = Gtk.Button(label="Help")
        self.button.connect("clicked", self.on_button_clicked)
        # Add the stuff together
        self.hb.pack_end(self.button)
        self.scroll.add(self.webview)
        self.add(self.scroll)
        # Generate and display the graph
        self.vis = visualizer.Visualizer()
        self.vis.create_graph(self.dirname, self.graph_name) 
        self.webview.open("file://localhost" + path.abspath(self.dirname) + "/" + self.graph_name+ ".svg")

    # TODO help window
    def on_button_clicked(self, widget):
        """ Function handling the Help button click"""
        help_win = HelpWindow()
        help_win.show_all()

    def show(self):
        """ Function for showing of Gui programatically"""
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        Gtk.main()

def usage():
    """ Prints usage instructions in cli"""
    print("How to use:")
    print("-h or --help: Prints this message.")
    print("-g or --gui: Starts the program in gui mode.")
    print("-d or --dir: Sets up the output directory.")
    print("  Example: sudo python3 gui.py -d output/")
    print("  Creates directory output and puts the graph.svg there")
    print("-n or --name: Sets up the name of output file.")
    print("  Example: sudo python3 gui.py -n graph")
    print("  Creates file called graph.svg")
    print("Running without any arguments creates graph with default name in default dir.")

def main():
    """ Main function of the program """
    is_gui = False
    dirname = "generated_graphs" 
    name = "graph"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hgd:n:", ["help", "gui", "dir=", "name="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-g", "--gui"):
            is_gui = True
            print("Running in GUI mode.")
        elif o in ("-d", "--dir"):
            dirname = a
        elif o in ("-n", "--name"):
            name = a
        else:
            assert False, "unhandled option"
    win = Gui(dirname, name)
    if is_gui:
        win.show()

class HelpWindow(Gtk.Window):
    """ Class hoding strings in help window """
    def __init__(self):
        Gtk.Window.__init__(self, title="Help")
        self.set_default_size(800,280)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_markup("<big>Graph help</big>\n"
                         "The Graph is zoomable and panable. You can also click on the nodes to receive additional information.\n"
                         "\n"
                         "<big>Nodes help</big>\n"
                         "The nodes have different shapes and colours according to the node type.\n"
                         "Nodes that are more hardware related are displayed with darker colour.\n"
                         "More abstract devices use brighter colour.\n"
                         "If there are actions present, red means delete action, green means create action and violet means resize.\n"
                         "\n"
                         "<big>Edges help</big>\n"
                         "The edges symbolize parent child relations.\n"
                         "Edges always go from parent to child for example sda -> sda1.\n"
                         "\n"
                         "<big>About this program</big>\n"
                         "This visualization tool was created as a bachelors thesis at <a href=\"https://www.fi.muni.cz/\">Faculty of Informatics</a> at <a href=\"https://www.muni.cz/\">Masaryk University</a>\n"
                         "with the help of people from <a href=\"https://www.redhat.com/en/global/czech-republic\">Red Hat Czech</a>, big thanks to them.\n"
                         "Pan and zoom functionality is provided by JS library <a href=\"https://code.google.com/archive/p/svgpan/\">SVGPan</a>.\n"
                         "<b>Author:</b> Václav Hodina\n"
                         "<b>E-mail:</b> vhodina@redhat.com\n"
                         "<b>Link</b> to <a href=\"https://github.com/vasekhodina/blivet_gv_visualization\">Github repository</a> of the project.\n")
        box.pack_start(label, True, True, 0)
        self.add(box)

if __name__ == "__main__":
    main()
