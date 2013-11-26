from flask import Flask, render_template, redirect, request, session, url_for
import model

app = Flask(__name__)
app.secret_key = "honeybooboochild"


@app.route("/")
def index():
	return render_template("index.html")
	

@app.route("/", methods=["POST"])
def logic():
	expression = request.form["logic-expression"]

	# in case an empty expression was passed
	if expression == "":
		return render_template("index.html")

	expression =  str("f = "+expression)
	print expression
	json = model.compile_expr(expression)
	return render_template(
		"schematic.html", 
		expression=expression, 
		json=json)

# @app.route("/ajax")

if __name__ == "__main__":
	app.run(debug=True)
