import os
# import json library so app can read data from json file
import json
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env


# creating instance of Flask class "app"
# app is Flask naming convention
# the first argument of the Flask class is the name of the app's module
# since we're just using one module we can use __name__ which is a
# built-in Python variable

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# app.route decorator. @ symbol - pie-notation
# browses to the root dir as indicated by "/"


@app.route("/")
# Flask triggers index function returns index.html
def index():
    # run render template function which is imported from Flask on line 3
    return render_template("index.html")
    # Flask looks for files (e.g. index.html) in a directory named "templates"


@app.route("/about")
def about():
    data = []
    # with block
    # open data/company.json as read only ("r"), and assign to
    # new variable "json_data"
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    # "company=data"
    # Assigns a new variable "company" that will be sent through to
    # the HTML template == the list of data it's loading
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}

    with open("data/company.json", "r") as json_data:
        # data - variable which holds loaded data in json format
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]))
        print("Hello Cuntyhooks {}".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

# python main function - function which interpreter runs first


if __name__ == "__main__":
    # we run our app using the arguments passed here
    # set debug to false before production / project submission
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
