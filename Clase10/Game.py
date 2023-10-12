class Game:
  def __init__(self,id,name,genre,year):
    self.id=id
    self.name=name
    self.genre=genre
    self.year=year

  def dump(self):
    return {
      "id":self.id,
      "name":self.name,
      "genre":self.genre,
      "year":self.year
    }
  