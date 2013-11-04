# Created by Ingrid Avendano 11/1/13.

# Lexer file that reads in VHDL code and parses it. 

FILENAME = "vhdl/and_gate.vhd"



def tokenize(code):
	pass


def find_ports(code):
	pass

## READIN AND FILTERING CODE ####################################

# finds open and closed brackets of code:
def bracketed_code(code):
	pass


def separate_sections(code):
	definition = [] 
	behavior = []
	pass


def filter_code(code):
	cleaner_code = []

	# removes blank lines of code and comments
	for line in code:
		if line != "" and not "--" in line:
			# remove use of libraries
			if not "library" in line and not "use" in line:
				cleaner_code.append(line)

	print_code(cleaner_code)
	return cleaner_code


def print_code(code):
	for line in code:
		print line


def read(file_name):
	vhdl_file = open(file_name)
	vhdl_code = vhdl_file.read()
	vhdl_file.close()

	lines_of_code = vhdl_code.split("\n")

	return lines_of_code


## MAIN #########################################################
def main():
	vhdl = read(FILENAME)
	# print_code(vhdl)
	vhdl = filter_code(vhdl)
	definition, behavior = separate_sections(vhdl)



if __name__ == "__main__":
	main()
