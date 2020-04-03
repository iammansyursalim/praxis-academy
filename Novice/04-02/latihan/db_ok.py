from flask import Flask, g
app = Flask(__name__)
with app.app_context():
    g.my_db = 'database ok'
    print(g.my_db)