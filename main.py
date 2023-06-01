from flask import Flask, render_template, url_for

site = Flask(__name__)

@site.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    site.run(debug=True)


