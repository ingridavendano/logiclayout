# Created by Ingrid Avendano 11/4/13.

# This file creates a JSON files of digital logic from VHDL.

import json


###############################################################################
def make_json_file(netlist, filename):
	filename = "./json/" + filename + ".json"
	json_file = open(filename, 'w')


	module = {
	"name": netlist.name,
	"ports": {
		"in": netlist.in_ports,
		"out": netlist.out_ports
		}
	}

	json_module = json.dumps(module, sort_keys=True, indent=4, separators=(',', ': '))

	json_file.write(json_module)

	json_file.close()
	


# ## MAIN #######################################################################
# def main():
# 	make_json_file("test","test")


# if __name__ == "__main__":
# 	main()