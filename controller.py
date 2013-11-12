from flask import Flask, render_template, redirect, request, session, url_for
# import model

app = Flask(__name__)
app.secret_key = "honeybooboochild"


@app.route("/")
def index():
	return render_template("index.html")
	

@app.route("/logic", methods=["POST"])
def logic():
	expression = request.form["logic-expression"]
	print "#"*80
	print expression
	return render_template("logic_expression.html", expression=expression)

if __name__ == "__main__":
	app.run(debug=True)
