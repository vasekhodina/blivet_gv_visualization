import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Rsvg', '2.0')
from gi.repository import Gtk, Rsvg, GdkPixbuf

import sys
import visualization


class Gui(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Disk data visualization")
		self.box = Gtk.Box(spacing=6)
		self.add(self.box)

		self.button = Gtk.Button(label="Do the magic!")
		self.button.connect("clicked", self.on_button_clicked)
		self.box.pack_start(self.button, True, True, 0)

	def on_button_clicked(self, widget):
		vis = visualization.Visualization()
		vis.createGraph("degraf")


		svg = Rsvg.Handle.new_from_file("degraf")
		loader = GdkPixbuf.PixbufLoader()
		pixbuf = svg.get_pixbuf()
		image = Gtk.Image.new_from_pixbuf(pixbuf)

		self.box.pack_start(image, True, True, 0)
		self.show_all()
		loader.close()

"""    def do_activate(self):
        # create a Gtk Window belonging to the application itself
        window = Gtk.Window(application=self)
        # set the title
        window.set_title("")
        # show the window
        window.show_all()
"""

# create and run the application, exit with the value returned by
# running the program
win = Gui()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
