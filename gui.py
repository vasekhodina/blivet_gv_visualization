import visualizer
import sys
import getopt
from os import path

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Rsvg', '2.0')
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, Rsvg, GdkPixbuf, WebKit


# TODO Clean up this flippin mess
class Gui(Gtk.Window):
    def __init__(self, dirname, graph_name):
        self.dirname = dirname
        self.graph_name = graph_name
        Gtk.Window.__init__(self, title="Disk data visualization")
        self.webview = WebKit.WebView()
        settings = self.webview.get_settings()
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.set_default_size(800, 600)
        self.layout = Gtk.Layout()
        self.layout.put(self.webview, 50, 50)
        self.layout.set_vexpand(True)
        self.layout.set_hexpand(True)

        self.button = Gtk.Button(label="Do the magic!")
        self.layout.put(self.button, 6, 6)
        self.button.connect("clicked", self.on_button_clicked)
        self.grid.attach(self.layout, 0, 0, 1, 1)

        vadjustment = self.layout.get_vadjustment()
        hadjustment = self.layout.get_hadjustment()
        vscrollbar = Gtk.Scrollbar(orientation=Gtk.Orientation.VERTICAL, adjustment=vadjustment)
        self.grid.attach(vscrollbar, 1, 0, 1, 1)
        hscrollbar = Gtk.Scrollbar(orientation=Gtk.Orientation.HORIZONTAL, adjustment=hadjustment)
        self.grid.attach(hscrollbar, 0, 1, 1, 1)

        self.vis = visualizer.Visualizer()
        self.vis.createGraph(self.dirname, self.graph_name) 
    def on_button_clicked(self, widget):
        self.webview.open("file://localhost" + path.abspath(self.dirname) + "/" + self.graph_name+ ".svg")

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

# create and run the application, exit with the value returned by
# running the program
# TODO Make the program react to the options
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
