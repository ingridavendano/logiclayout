
from compiler import run

def compile_expr(expr):
	# run.clear_parser()
	return run.compiler(expr)


if __name__ == "__main__":

	expr = "f = a * (b OR (NOT (c * (NOT i)))) xor (d | c | g) xor (s OR t) xor (NOT (a OR (NOT (u and p)))) and f"
	# expr = "f = (a + b) and c"
	tree = run.compiler(expr)

	# tree.print_tree()