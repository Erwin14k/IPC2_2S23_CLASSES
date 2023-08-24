from nodo_carcel import nodo_carcel
from grupo import grupo
class lista_carceles:
  def __init__(self):
    self.primero = None
    self.contador_carceles=0

  def insertar_dato(self,carcel):
    if self.primero is None:
      self.primero = nodo_carcel(carcel=carcel)
      self.contador_carceles+=1
      return
    actual= self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo_carcel(carcel=carcel)
    self.contador_carceles+=1

  def recorrer_e_imprimir_lista(self):
    print("Total De cárceles almacenadas: ",self.contador_carceles)
    print("")
    print("")
    print("")
    print("*******************************************************************************************")
    actual = self.primero
    while actual != None:
      print("Nombre:",actual.carcel.nombre,"Niveles:",actual.carcel.niveles," Celdas por nivel:",actual.carcel.celdas_por_nivel)
      actual.carcel.lista_celdas.recorrer_e_imprimir_lista()
      actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
      actual = actual.siguiente
      print("")
      print("")
      print("")
    print("*******************************************************************************************")
    print("")
    print("")
    print("")

  def calcular_los_patrones(self,nombre_carcel):
    # recorremos la lista de carceles hasta encontrar una coincidencia
    actual = self.primero
    while actual != None:
      # Si entra al if, es por que encontramos la carcel que queremos
      if actual.carcel.nombre==nombre_carcel:
        # Obtenemos sus patrones
        actual.carcel.lista_patrones_nivel=actual.carcel.lista_patrones_celdas.devolver_patrones_por_nivel(actual.carcel.lista_patrones_nivel)
        # Imprimimos todos sus patrones
        actual.carcel.lista_patrones_nivel.recorrer_e_imprimir_lista()
        # obtenemos los grupos
        lista_patrones_temporal=actual.carcel.lista_patrones_nivel
        grupos_sin_analizar=lista_patrones_temporal.encontrar_coincidencias()
        # Este es un string, por ejemplo "1,2--3,5--4"
        print(grupos_sin_analizar)
        # por cada grupo recorrer la matriz original e ir devolviendo las coordenadas especificadas
        #recordando que por cada coincidencia encontrada, se va borrando para dejar solo las que no tienen grupo.
        buffer=""
        for digito in grupos_sin_analizar:
          if digito.isdigit() or digito==",":
            buffer+=digito
          elif digito =="-" and buffer!="":
            cadena_grupo=actual.carcel.lista_celdas.devolver_cadena_del_grupo(buffer)
            actual.carcel.lista_grupos.insertar_dato(grupo=grupo(buffer,cadena_grupo))
            buffer=""
          else:
            buffer=""
        actual.carcel.lista_grupos.recorrer_e_imprimir_lista()

        
        return
      actual=actual.siguiente
    print ("No se encontró la carcel")