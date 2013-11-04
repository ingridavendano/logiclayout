# Created by Ingrid Avendano on 11/1/13.

# This file contains the netlist classes needed for circuits. 

class Circuit:
	def __init__(self, name=""):
		self.name = name 


class Netlist(Circuit):
	ports = None
	modules = None
	nets = None


class Module(Circuit):
	netlist = None
	submodules = None
	cells = None
	ports = None

class Port(Circuit):
	netlist = None
	module = None
	direction = None


class Cell(Circuit):
	netlist = None
	in_pins = None
	out_pins = None
	logic = None

class Pin(Circuit):
	netlist = None
	signal = None
	ins = None
	outs = None
	ports = None
	nets = None

