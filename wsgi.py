from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def home():
    return render_template("home.html")

@application.route("/about")
def home():
    return render_template("about.html")

@application.route("/world")
def hello():
    return "Hello World!"

@application.route("/test")
def test():
    return "This is a test"



if __name__ == "__main__":
    application.run()
