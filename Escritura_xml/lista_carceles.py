from nodo_carcel import nodo_carcel
from grupo import grupo
import xml.etree.ElementTree as ET
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

  def generar_xml_salida(self):
    # creación del xml de salida
    mis_carceles=ET.Element("MisCarceles")
    # Crear un sub elemento <ListaCarceles> que le pertenezca a <misCarceles>
    lista_carceles=ET.SubElement(mis_carceles,"listaCarceles")
    # Recorremos nuestra lista de carceles
    actual=self.primero
    while actual!=None:
      # Crear un sub elemento <Carcel> que le pertenezca a <listaCarceles>
      carcel=ET.SubElement(lista_carceles,"Carcel")
      # Crear un sub elemento <nombre> que le pertenezca a <Carcel>
      nombre=ET.SubElement(carcel,"nombre")
      nombre.text=actual.carcel.nombre
      # Crear un sub elemento <niveles> que le pertenezca a <Carcel>
      niveles=ET.SubElement(carcel,"niveles")
      niveles.text=str(actual.carcel.niveles)
      # Recorremos la lista patrones (0 y 1) de la carcel
      actual_lista_patrones=actual.carcel.lista_patrones_celdas.primero
      lista_patrones=ET.SubElement(carcel,"listaPatrones")
      
      while actual_lista_patrones!=None:
        # Crear un sub elemento <niveles> que le pertenezca a <Carcel>
        dato=ET.SubElement(lista_patrones,"listaPatrones")
        dato.text=str(actual_lista_patrones.celda.prisionero)
        actual_lista_patrones=actual_lista_patrones.siguiente
      actual=actual.siguiente

      #Generar xml
      my_data=ET.tostring(mis_carceles)
      my_data=str(my_data)
      self.xml_arreglado(mis_carceles)

      arbol_xml=ET.ElementTree(mis_carceles)
      arbol_xml.write("./Escritura_xml/Reportes/salida.xml",encoding="UTF-8",xml_declaration=True)
  
  def xml_arreglado(self, element, indent='  '):
    # Inicializar una cola con el elemento raíz y nivel de anidación 0
    queue = [(0, element)]  # (level, element)
    # Bucle principal: continúa mientras haya elementos en la cola
    while queue:
      # Extraer nivel y elemento actual de la cola
      level, element = queue.pop(0)
      # Crear tuplas para cada hijo con nivel incrementado
      children = [(level + 1, child) for child in list(element)]
      # Agregar saltos de línea e indentación al inicio del elemento actual
      if children:
        element.text = '\n' + indent * (level + 1)
        # Agregar saltos de línea e indentación al final del elemento actual
      if queue:
        element.tail = '\n' + indent * queue[0][0]
      else:
        # Si este es el último elemento del nivel actual, reducir la indentación
        element.tail = '\n' + indent * (level - 1)
      # Insertar las tuplas de hijos al principio de la cola
      queue[0:0] = children





  


  
