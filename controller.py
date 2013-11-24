from flask import Flask, render_template, redirect, request, session, url_for
import model

app = Flask(__name__)
app.secret_key = "honeybooboochild"


@app.route("/")
def index():
	return render_template("index.html")
	

@app.route("/logic", methods=["POST"])
def logic():
	expression = request.form["logic-expression"]
	print "#"*80
	expression =  str("f = "+expression)
	print expression
	json = model.compile_expr(expression)
	return render_template(
		"schematic.html", 
		expression=expression, 
		json=json)
	# return json

# @app.route("/ajax")

if __name__ == "__main__":
	app.run(debug=True)
