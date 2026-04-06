
# module 10 - Flask Application
# Meghan Cullen 4/6/2026

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/meghan")
def meghan():
    x = 6
    y = 15
    z = x + y 
    name = "Meghan"
    return f"Hello {name}, the sum of {x} and {y} is {z}"
    
@app.route("/about")
def about():
     return render_template("about.html")

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5002, debug=True)