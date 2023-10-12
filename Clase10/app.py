from flask import Flask
from flask_cors import CORS
from Game_DAO import Game_DAO
from flask.globals import request

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



if __name__ == '__main__':
  app.run(threaded=True,port=5000,debug=True)
