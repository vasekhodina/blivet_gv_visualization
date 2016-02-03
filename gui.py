from gi.repository import Gtk
import sys
import rsvg


class Gui(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Disk data visualization")
		self.button = Gtk.Button(label="Do the magic!")
		self.button.connect("clicked", self.on_button_clicked)
		self.add(self.button)

	def on_button_clicked(self, widget):
		print("Hello World")
		svg = rsvg.Handle(file="graf")
		win.connect("expose-event", svg)
		win.show_all()
		

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
