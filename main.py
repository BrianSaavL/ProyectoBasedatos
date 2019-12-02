from flask import Flask, render_template, request, abort, json
from pymongo import MongoClient
import pandas as pd
import os

USER_KEYS = ['name', 'last_name', 'occupation', 'follows', 'age']

# El cliente se levanta en la URL de la wiki
URL = "mongodb://grupo80:grupo80@gray.ing.puc.cl/grupo80"
client = MongoClient(URL)
db = client.get_database()


# Iniciamos la aplicación de flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>HELLO</h1>"

# Mapeamos esta función a la ruta '/messages' con el método get.
@app.route("/messages")
def get_body():
    identificador = request.args.get('id', False)
    message = db.mensajes.find_one({'id': identificador}, {'_id': 0})
    return json.jsonify(message)

if __name__ == "__main__":
    app.run()
