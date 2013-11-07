# Created by Ingrid Avendano 11/1/13.

# Lexer file that reads in VHDL code and parses it. 

from netlist import Module
import make_graphviz
import make_json

## SPECIAL VARIABLES ##########################################################
FILE_NAME = "and_gate"
FILE_PATH = "hdl/vhdl/" + FILE_NAME + ".vhd"
COMMENTED_CODE = "--"



## READIN AND FILTERING CODE ##################################################
def separate_sections(code):
	definition = [] 
	behavior = []
	
	# figuring out the definition of a circuit by finding the beginning
	# and ending points of a circuit
	def_begin = def_end = False
	architecture_section = False

	for line in code:
		if "entity" in line:
			def_begin = True

		# adds line of definition code
		if def_begin and not def_end:
			definition.append(line)

		if "end" in line:
			def_end = True

		if "architecture" in line:
			architecture_section = True

		if architecture_section: 
			behavior.append(line)

	mod = Module(definition)
	mod.show()
	

	return mod



def filter_code(code):
	cleaner_code = []

	# removes blank lines of code and comments
	for line in code:
		if line != "" and not COMMENTED_CODE in line:
			# remove use of libraries
			if not "library" in line and not "use" in line:
				cleaner_code.append(line)

	return cleaner_code


def print_code(code):
	print ""
	print "#"*80
	for line in code:
		print line
	print "#"*80
	print ""


def read(file_name):
	vhdl_file = open(file_name)
	vhdl_code = vhdl_file.read()
	vhdl_file.close()

	lines_of_code = vhdl_code.split("\n")

	return lines_of_code


## MAIN #######################################################################
def main():
	vhdl = read(FILE_PATH)
	vhdl = filter_code(vhdl)
	module = separate_sections(vhdl)
	make_graphviz.make_graphviz_file(module, FILE_NAME)
	make_json.make_json_file(module, FILE_NAME)


if __name__ == "__main__":
	main()
