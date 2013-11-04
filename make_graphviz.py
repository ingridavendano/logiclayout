# Created by Ingrid Avendano 11/4/13.

# This file creates Graphviz dot files of digital logic from VHDL.

# import lex.py

from sys import argv






## MAIN #########################################################
def main():
	script, filename = argv

	print filename[0]

	# filename = "/graphs/" + filename + ".gv"
	# graphviz = open(filename, 'w')

	# f.close()


if __name__ == "__main__":
	main()