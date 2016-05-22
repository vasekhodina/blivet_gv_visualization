# This script created actions graph with two actions in this dir called actions.svg
# You can open it in browser to see if the graph generated correctly
### IMPORTANT ###
# Before running this file please create a device file loop0 using dd and losetup
# The disk can be about 30 MB in size
import sys
sys.path.append("./..")

import blivet
import visualizer
from blivet.size import Size

b = blivet.Blivet()
b.reset()
loop = b.devicetree.getDeviceByName("loop0")
b.destroyDevice(loop)
v = visualizer.Visualizer(blivet=b, palletePath="../assets/pallete.xml")
v.create_actions_graph(".", "actions")
