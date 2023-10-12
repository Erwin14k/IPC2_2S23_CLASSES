from flask import Flask
from flask_cors import CORS
from Game_DAO import Game_DAO
from flask.globals import request
import xml.etree.ElementTree as ET
import base64

game_handler= Game_DAO()
app= Flask(__name__)
CORS(app)

game_handler.new_game("God of war Ragnarok","Action","2022")
game_handler.new_game("Uncharted 4 a Thief´s end","Adventure","2016")
game_handler.new_game("Call of duty Black ops 3","Action","2015")
game_handler.new_game("Far cry 5","Adventure","2018")

@app.route("/")
def index():
  return "<h1> Hello from backend! </h1>"

@app.route("/new-game",methods=['POST'])
def new_game():
  response={}
  name=request.json['name']
  genre=request.json['genre']
  year=request.json['year']
  if(game_handler.new_game(name,genre,year)):
    response={
      "state":"perfect",
      "message":"El juego fue creado con éxito!"
    }
    return response
  else:
    response={
      "state":"Error",
      "message":"El juego ya existe en mi base de datos!"
    }
    return response
  

@app.route("/games-by-genre/<genre>",methods=['GET'])
def games_by_genre(genre):
  return game_handler.games_by_genre(genre)


@app.route("/games-by-year/<year>",methods=['GET'])
def games_by_year(year):
  return game_handler.games_by_year(year)




@app.route("/archive",methods=['POST'])
def file_upload():
  response={}
  # Obtenemos el xml codificado
  xml=request.json['xmlFile']
  # Lo de codificamos
  xml_bytes = base64.b64decode(xml)
  # Lo formateamos a utf-8
  xml_string=xml_bytes.decode('utf-8')
  root=ET.fromstring(xml_string)
  #Lectura del xml
  for carcel_temporal in root.findall('carcel'):
  # Obtener atributos principales (nombre, niveles, celdas_por_nivel)
    nombre_carcel=carcel_temporal.get('nombre')
    niveles_carcel=carcel_temporal.get('nivel')
    celdas_por_nivel=carcel_temporal.get('numeroCelda')
    for celda_carcel in carcel_temporal.findall('celda'):
      nivel_celda=celda_carcel.get('nivel')
      numero_celda=celda_carcel.get('numeroCelda')
      prisionero_celda=celda_carcel.text
      print("Celda",nivel_celda,numero_celda,prisionero_celda)
    print("CARCEL",nombre_carcel,niveles_carcel,celdas_por_nivel)
  response={
      "state":"perfect",
      "message":"El archivo fue leido con éxito"
  }
  return response




if __name__ == '__main__':
  app.run(threaded=True,port=5000,debug=True)
