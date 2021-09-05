from flask import Blueprint

appBlueprint = Blueprint("home",__name__)
@appBlueprint.route("/")
def index():
    return 'Hellow I am Nattawut'