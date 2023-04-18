from flask import Flask
from config import config
from .routes import prt

app = Flask(__name__, static_folder=config.STACTIC_FOLDER, template_folder= config.TEMPLATE_FOLDER)
app.config.from_object(config)

@app.route("/start")
def hello():
    return "<p>Hello Wordl </p>"


#Manejo de BluePrints
app.register_blueprint(prt, url_prefix="/")

