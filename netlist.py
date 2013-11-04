# Created by Ingrid Avendano on 11/1/13.

# This file contains the netlist classes needed for circuits. 

class Circuit:
	def __init__(self, name=""):
		self.name = name 


class Module(Circuit):
	in_ports = []
	out_ports = []

	def __init__(self, code):
		# gets the name of the module
		first_line = code[0].split()
		self.name = first_line[1]

		# separates in and out ports
		for line in code[1:-1]:
			if ":" in line: 
				# creats list of name and direction of ports
				ports = line.split(":")
				name = ports[0].split()[-1]
				direction = ports[1].split()[0]

				if direction == "in":
					self.in_ports.append(name)
				elif direction == "out":
					self.out_ports.append(name)
	
	def show(self):
		print "Module name:", self.name
		print "   IN ports:", self.in_ports
		print "  OUT ports:", self.out_ports