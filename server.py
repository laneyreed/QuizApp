from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


#****************************HTML Routes*****************************************
@app.route("/html")
def html_home():
    return render_template("html/html-home.html")


#****************************CSS Routes*****************************************
@app.route("/css")
def css_home():
    return render_template("css/css-home.html")

@app.route("/css_concept/display")
def css_display():
    return render_template("./css/fundamentals/display.html")

@app.route("/css-concept/<concept>")
def css_concept(concept):
    return render_template("./css/css-concept.html", concept=concept)


#****************************JavaScript Routes*****************************************
@app.route("/javascript")
def javascript_home():
    return render_template("js/javascript.html")


#****************************Python Routes*****************************************
@app.route("/python")
def python_home():
    return render_template("python/python.html")

if __name__ == "__main__":
    app.run(debug=True)