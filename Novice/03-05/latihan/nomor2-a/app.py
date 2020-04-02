from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    # defining function
    return render_template("404.html")


if __name__ == '__main':
    app.run(debug=True)
