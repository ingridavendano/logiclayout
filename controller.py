# -----------------------------------------------------------------------------
# controller.py
# Created by Ingrid Avendano 11/17/13.
# -----------------------------------------------------------------------------
# Contols different views and runs model depending on the view.
# -----------------------------------------------------------------------------

import os
from flask import Flask, render_template, request
import model

# -----------------------------------------------------------------------------

app = Flask(__name__)
app.secret_key = "honeybooboochild"

# -----------------------------------------------------------------------------
# Run main view of website showing no sublinks.
# -----------------------------------------------------------------------------


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def new_logic():
    data = request.form["logic-expression"]

    # in case an empty expression was passed
    if data.strip() == "":
        return render_template("index.html")

    data = str("f = " + data)
    json = model.compile_expr(data)

    if json is not None:
        return render_template(
            "index.html",
            expr=data,
            display=True,
            json=json)
    else:
        return render_template("index.html", expr="try again")


@app.route("/explain", methods=["GET"])
def explain():
    return render_template("explain.html")

# -----------------------------------------------------------------------------

if __name__ == "__main__":

    port = int(os.getenv('CIRCUIT_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
