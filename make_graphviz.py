# Created by Ingrid Avendano 11/4/13.

# This file creates Graphviz dot files of digital logic from VHDL.


###############################################################################
def make_graphviz_file(netlist, filename):

	filename = "./graphs/" + filename + ".gv"
	graphviz = open(filename, 'w')

	base = """digraph Netlist {
	rankdir = LR;

	"""
	graphviz.write(base)

	for in_port in netlist.in_ports:
		line = "\t" + in_port + " -> " + netlist.name + ";\n"
		graphviz.write(line)

	for out_port in netlist.out_ports:
		line = "\t" + netlist.name  + " -> " + out_port + ";\n"
		graphviz.write(line)

	graphviz.write("}\n")

	graphviz.close()
