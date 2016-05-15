import visualizer
import sys
from os import path

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Rsvg', '2.0')
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, Rsvg, GdkPixbuf, WebKit


# TODO Clean up this flippin mess
class Gui(Gtk.Window):
    def __init__(self):
        self.VAR_DIR = "./var/"
        self.GRAPH_NAME = "degraf"
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
        self.vis.createGraph(self.GRAPH_NAME, self.VAR_DIR) 
    def on_button_clicked(self, widget):
        self.webview.open("file://localhost" + path.abspath(self.VAR_DIR) + "/" + self.GRAPH_NAME + ".svg")

# create and run the application, exit with the value returned by
# running the program
if __name__ == "__main__":
    win = Gui()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
