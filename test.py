
from compiler import run

def compile_expr(expr):
	# run.clear_parser()
	return run.compiler(expr)


if __name__ == "__main__":

	# expr = "f = a * (b OR (NOT c)) xor (d | c | g) xor (s OR t)"
	expr = "f = a * (b OR (NOT (c * (NOT i)))) xor (d | c | g) xor (s OR t) xor (NOT (a OR (NOT (u and p)))) and f"
	run.compiler(expr)


	# expr1 = "w = not f"

	# expr2 = "z = w and f"

	# expr3 = "w"

	# # for expr in [expr0, expr1, expr2, expr3]:
	# 	# print expr
	# # compile_expr([expr0, expr1, expr2, expr3])
	# compile_expr([expr0])