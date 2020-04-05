from flask import Flask
from .api import api

app = Flask(__name__)

# Puts the API blueprint on api.U2FtIEJsYWNr.com.
app.register_blueprint(api, subdomain='api')