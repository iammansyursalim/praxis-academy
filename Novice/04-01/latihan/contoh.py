from flask import Flask, Response
import json

app = Flask('rest api')

@app.route('/')
def index():
    data = {
        "message": "hello world"
    }
    data_json = json.dumps(data)
    return Response(data_json, mimetype='application/json')

app.run(debug=True)