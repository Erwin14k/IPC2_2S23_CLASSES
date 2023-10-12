from Game import Game
import json

class Game_DAO:
  def __init__(self):
    self.games=[]
    self.id_counter=1


  # Función para agregar nuevos juegos
  def new_game(self,name,genre,year):
    for game in self.games:
      if game.name==name:
        return False
    new=Game(self.id_counter,name,genre,year)
    self.games.append(new)
    self.id_counter+=1
    return True
  
  # Función para devolver los juegos en base a su género
  def games_by_genre(self,genre):
    return json.dumps([Game.dump() for Game in self.games if Game.genre==genre],indent=4)
  
  # Función para devolver los juegos en base a su género
  def games_by_year(self,year):
    return json.dumps([Game.dump() for Game in self.games if Game.year==year],indent=4)

