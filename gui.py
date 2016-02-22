import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Rsvg', '2.0')
from gi.repository import Gtk, Rsvg, GdkPixbuf

import sys
import visualization


class Gui(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Disk data visualization")
		self.grid = Gtk.Grid()
		self.add(self.grid)
		self.set_default_size(800,600)
		self.layout = Gtk.Layout()
		self.layout.set_vexpand(True)
		self.layout.set_hexpand(True)	

		self.button = Gtk.Button(label="Do the magic!")
		self.layout.put(self.button, 6,6)
		self.button.connect("clicked", self.on_button_clicked)
		
		self.grid.attach(self.layout, 0, 0, 1, 1)

		vadjustment = self.layout.get_vadjustment()
		hadjustment = self.layout.get_hadjustment()
		vscrollbar = Gtk.Scrollbar(orientation=Gtk.Orientation.VERTICAL, adjustment=vadjustment)
		self.grid.attach(vscrollbar, 1, 0, 1, 1)
		hscrollbar = Gtk.Scrollbar(orientation=Gtk.Orientation.HORIZONTAL, adjustment=hadjustment)
		self.grid.attach(hscrollbar, 0, 1, 1, 1)
		
		self.vis = visualization.Visualization()
		self.vis.createGraph("degraf")
		self.svg = Rsvg.Handle.new_from_file("degraf")


	def on_button_clicked(self, widget):
		loader = GdkPixbuf.PixbufLoader()
		pixbuf = self.svg.get_pixbuf()
		image = Gtk.Image.new_from_pixbuf(pixbuf)
		svg_dimensions = self.svg.get_dimensions()
		self.layout.set_size(svg_dimensions.width + 30,svg_dimensions.height + 50)
		self.layout.put(image, 20, 40)
		self.show_all()
		loader.close()

# create and run the application, exit with the value returned by
# running the program
win = Gui()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
