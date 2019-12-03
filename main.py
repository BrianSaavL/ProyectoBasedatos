from flask import Flask, render_template, request, abort, json
from pymongo import MongoClient
import pandas as pd
import os

USER_KEYS = ['id', 'content', 'metadata']

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

@app.route("/messages", methods=["DELETE"])
def delete_email():
    identificador = request.args.get('id', False)
    result = db.mensajes.delete_one({'id': identificador})
    if (result):
        message = "1 usuario eliminado"
        success = True
    else:
        message = "No se pudo eliminar el usuario"
        success = False
    return json.jsonify({'success': success, 'message': message})

@app.route("/messages/project-search")
def get_project():
    nombre = request.args.get('nombre', False)
    info = [u for u in db.mensajes.find({"$or": [{'metadata.sender': nombre}, {'metadata.receiver':nombre}]}, {'_id': 0})]
    return json.jsonify(info)

@app.route("/messages", methods=['POST'])
def create_email():
    data = request.get_json()
    # Insertar retorna un objeto
    result = db.mensajes.insert_one(data)
    # Creo el mensaje resultado
    if (result):
        message = "1 usuario creado"
        success = True
    else:
        message = "No se pudo crear el usuario"
        success = False
    # Retorno el texto plano de un json
    return json.jsonify({'success': success, 'message': message})

if __name__ == "__main__":
    app.run()
