from flask import Flask,jsonify,request
from flask_cors import CORS
import re
import base64
app= Flask(__name__)
CORS(app)

@app.route('/upload_file',methods=['POST'])
def upload_file():
  if 'file' not in request.files:
    return jsonify({
      "message": "No se ha enviado un archivo, intente de nuevo :("
    })
  file = request.files['file']
  # leer el contenido del archivo
  # Ahora el contenido lo convertimos a un string
  file_contents=file.read().decode('utf-8')
  # Print del contenido
  print(file_contents)
  return jsonify({
      "message": "El archivo fue cargado exitosamente y fue leido:)"
    })  

@app.route('/flask_response',methods=['GET'])
def get_response_from_flask():
  response_data={"message":"Mañana es feriado"}
  return jsonify(response_data)


@app.route('/flask_response2',methods=['GET'])
def get_response_from_flask2():
  response_data={"message":"Nos vemos del otro lado!"}
  return jsonify(response_data)



if __name__=="__main__":
  app.run(threaded=True,port=5000,debug=True)




