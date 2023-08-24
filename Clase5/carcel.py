class carcel:
  def __init__(self,nombre,niveles,celdas_por_nivel,lista_celdas,lista_patrones_celdas,lista_patrones_nivel,lista_grupos):
    self.niveles = niveles
    self.celdas_por_nivel = celdas_por_nivel
    self.lista_celdas=lista_celdas
    self.nombre=nombre
    self.lista_patrones_celdas=lista_patrones_celdas
    self.lista_patrones_nivel=lista_patrones_nivel
    self.lista_grupos=lista_grupos