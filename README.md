Para correr la aplicación primero se deben seguir los pasos del README.md presente en la ayudantía de APIs.
Luego, usando postman se pueden probar las diferentes rutas programadas. A continuación presentamos las rutas programadas y especificaciones de cómo probarlas.

Presentamos aquí dos documentos presentes en la base de datos del servidor
    {
    "content": "hola pymongo",
    "id": "A12", 
    "metadata": 
    { 
    "receiver": "perez",
    "sender": "juan",
    "time": "2019-04-17 05:20:37"
    }
    }
y 
{
 "id": "Am6FA24F",
 "content": "Hola socio tanto tiempo, como estas?. Te cuento que seguimos
  operando a pesar de que aprobaron un recurso de proteccion
  en nuestra contra. Nadie ha venido a fiscalizar esta mina de
cobre haha. Espero que tengas la misma suerte con tu
termoelectrica en Antofagasta amigo mi. Saludos!",
"metadata": 
{
"time": "2019-04-17 05:20:37",
"sender": "Franke",
"receiver": "Anheuser-Busch Inbev SA"
}
}


# Rutas:
- Con request de tipo GET:
--  **/messages/:id**:  para usar esta ruta escribir en postman la url seguida de /messages? y luego una id. Por     ejemplo: http://127.0.0.1:8000/messages?id=Am6FA24F.
 -- **/messages/project-search**:  para usar esta ruta escribir en postman la url seguida de /messages/project-search? y luego un nombre. Por ejemplo:
 http://127.0.0.1:8000/messages/project-search?nombre=juan
 http://127.0.0.1:8000/messages/project-search?nombre=perez
 http://127.0.0.1:8000/messages/project-search?nombre=Franke

  --**/messages/content-search**: para usar esta ruta escribir la url en postman, seguido de /messages/content-search, y luego en el body, escribir un JSON. Ejemplos:
{"desired": []"required": ["hola"],"forbidden": []}
{"desired": [], "required": ["hola"], "forbidden": ["pymongo"]}
{"desired": [], "required": ["hola", "pymongo"], "forbidden": []}
{"desired": [], "required": [], "forbidden": []}
- Con request de tipo POST:
  --**/messages**; Agregar en el body un correo en el formate de los anteriormente mostrados, en modo application/jason.
 Con request de tipo DELETE:
--**/messages/:id**; para usar esta ruta escribir en postman la url seguida de /messages? y luego una id existente para eliminarla de la base.

