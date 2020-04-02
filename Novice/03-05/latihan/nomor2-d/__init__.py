from flask import Flask, render_template, flash
import Content

TOPIC_DICT = Content()

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html", TOPIC_DICT=TOPIC_DICT)


@app.route('/slashboard/')
def slashboard():
    try:
        return render_template("dashboard.html", TOPIC_DICT=shamwow)
    except Exception as e:
        return render_template("500.html", error=str(e))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)
