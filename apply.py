# Student Name: Timothy Kim
# Titan Email: tk-im@csu.fullerton.edu
# Project: CSPC 335 - Interactive Campus Navigation System
# Date: 10/24/25

from tkinter import *
from tkinter import ttk

#Nodes
class Building:
	def __init__(self, name):
		self.name = name

#Edges
class Path:
	def __init__(self, dist, time, access):
		self.dist, self.time, self.access = dist, time, access
	
	#input must already be validated atp
	def set_time(self, newtime):
		self.time = newtime
		
	def set_access(self, newaccess):
		self.access = newaccess

class System:
	buildings = []
	building_error = ""
	
	paths = []
	
	def __init__(self, root):
		"""Frame for the UI elements"""
		ui_frame = ttk.Frame(root, padding=(30, 30, 30, 30))
			#"Frame" widget whose parent widget is the tkinter app window
			#padding with arbitrary pixel values
			
		ui_frame.grid(column = 0, row = 0, sticky=(N, W, E, S))
			#turn the UI frame into a grid with rows and cols

		"""Making a new Building"""
		ttk.Label(ui_frame, text = "Enter Building Name:").grid(column = 1, row = 1, sticky=(W, E))
			#label widget whose parent is the UI frame
			#placed in col 1, row 1

		self.new_building = StringVar()

		building_entry = ttk.Entry(ui_frame, width = 16, textvariable = self.new_building)
			#textbox (AKA entry) widget whose parent is the UI frame
			#textbox has a width of 16 characters
			#user input goes into newbuilding
		building_entry.grid(column = 1, row = 2, sticky=(W, E))
		
		ttk.Label(ui_frame, text = self.building_error).grid(column = 1, row = 3, sticky=(W, E))

		ttk.Button(ui_frame, text = "Add Building").grid(column = 1, row = 4, sticky=(W, E))
			#button widget that calls make_building() when clicked



		#Polish
		#expand to fill if window is resized
		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)
		
	def make_building():
		if newBuilding == "":
			self.building_error = "Error: No building name given"
		elif buildings.count(Building(newBuilding)) != 0:
			self.building_error.set("Error: Building already exists")
		else:
			buildings.append(Building(newbuilding))

#Run Tkinter program
root = Tk()
System(root)
root.mainloop()
