from flask import *
from werkzeug.utils import *

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template("upload_form.html")

@app.route('/sukses', methods=['POST'])
def sukses():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template('sukses.html',name = f.filename)

if __name__ == '__main__':
    app.run(debug=True)