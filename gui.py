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
        self.vis.createGraph(self.dirname, self.graph_name) 
        self.webview.open("file://localhost" + path.abspath(self.dirname) + "/" + self.graph_name+ ".svg")

    # TODO help window
    def on_button_clicked(self, widget):
        return

    def show(self):
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        Gtk.main()

def usage():
    print("How to use:")
    print("-h or --help: Prints this message.")
    print("-g or --gui: Starts the program in gui mode.")
    print("-d or --dir: Sets up the output directory.")
    print("  Example: sudo python3 gui.py -d output/")
    print("  Creates directory output and puts the graph.svg there")
    print("-n or --name: Sets up the name of output file.")
    print("  Example: sudo python3 gui.py -n graph")
    print("  Creates file called graph.svg")
    pritn("Running without any arguments creates graph with default name in default dir.")

def main():
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
    print("Output directory is: " + dirname)
    print("Name of the graph file: " + name)
    win = Gui(dirname, name)
    if is_gui:
        win.show()

if __name__ == "__main__":
    main()
