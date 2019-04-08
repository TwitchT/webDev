from flask import Flask
from flask import render_template
from flask import request

app = Flask(_name_)

@app.route("/hello")
def index():
    name = request.args.get('name', 'Nobody')
    
    if name:
            greeting = f"Hello, {name}"
        else:
            greeting = "Hello World"
        
        return render__template("index.html", greeting=greeting)

if _name_=="_main_":
    app.run()