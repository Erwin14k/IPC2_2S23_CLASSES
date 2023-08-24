import sys
import os
from nodo_celda import nodo_celda
from Patron import Patron
class lista_celdas:
  def __init__(self):
    self.primero = None
    self.contador_celdas=0

  def insertar_dato(self,celda):
    if self.primero is None:
      self.primero = nodo_celda(celda=celda)
      self.contador_celdas+=1
      return
    actual= self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo_celda(celda=celda)
    self.contador_celdas+=1

  def insertar_dato_ordenado(self, celda):
        nueva_celda = nodo_celda(celda=celda)
        self.contador_celdas += 1
        # Si la lista está vacía solo añade el nuevo nodo
        if self.primero is None:
            self.primero = nueva_celda
            return
        # Caso especial: la nueva celda debe ser el nuevo primer nodo, debe reemplazar al primero
        if celda.nivel < self.primero.celda.nivel or (
                celda.nivel == self.primero.celda.nivel and celda.numero_celda <= self.primero.celda.numero_celda):
            nueva_celda.siguiente = self.primero
            self.primero = nueva_celda
            return
        # Si no cumple con ninguno de los casos, recorrer hasta encontrar su posición
        actual = self.primero
        while actual.siguiente is not None and (
                celda.nivel > actual.siguiente.celda.nivel or (
                        celda.nivel == actual.siguiente.celda.nivel and celda.numero_celda > actual.siguiente.celda.numero_celda)):
            actual = actual.siguiente
        nueva_celda.siguiente = actual.siguiente
        actual.siguiente = nueva_celda

  def recorrer_e_imprimir_lista(self):
    print("===========================================================================================")
    actual = self.primero
    while actual != None:
      print(" Nivel: ",actual.celda.nivel,"No. Celda: ",actual.celda.numero_celda," Prisionero:",actual.celda.prisionero)
      actual = actual.siguiente
    print("===========================================================================================")

  # método para devolver los patrones por nivel
  def devolver_patrones_por_nivel(self,lista_patrones_nivel):
    actual = self.primero
    sentinela_de_filas=actual.celda.nivel #iniciaria en 1
    fila_iniciada=False
    recolector_patron=""
    while actual != None:
      # si hay cambio de fila entramos al if
      if  sentinela_de_filas!=actual.celda.nivel:
        # fila iniciada se vuelve false, por que se acaba la fila
        fila_iniciada=False
        # ya que terminamos la fila, podemos guardar los patrones
        lista_patrones_nivel.insertar_dato(Patron(sentinela_de_filas,recolector_patron))
        recolector_patron=""
        # actualizamos el valor de la fila (nivel)
        sentinela_de_filas=actual.celda.nivel
      # si fila iniciada es false, quiere decir que acaba de terminar fila y debemos empezar una nueva
      if fila_iniciada==False:
        fila_iniciada=True
        #Recolectamos el valor, ya que estamos en la fila
        recolector_patron+=str(actual.celda.prisionero)+"-"
      else:
        #Recolectamos el valor, ya que estamos en la fila
        recolector_patron+=str(actual.celda.prisionero)+"-"
      actual = actual.siguiente
    # Agregamos un nuevo patrón, sería el de toda la fila, ej: 0-1-1-1
    lista_patrones_nivel.insertar_dato(Patron(sentinela_de_filas,recolector_patron))
    # devolvermos la lista llena con los patrones
    return lista_patrones_nivel

  def generar_grafica(self,nombre_carcel,niveles,celdas_por_nivel):
    f = open('Lectura_xml/bb.dot','w')
    text ="""
        digraph G {"t="""+niveles+"""","A="""+celdas_por_nivel+""""->" """+nombre_carcel+ """" bgcolor="#3990C4" style="filled"
        subgraph cluster1 {fillcolor="blue:red" style="filled"
        node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
        a0 [ label=<
        <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
    actual = self.primero
    sentinela_de_filas=actual.celda.nivel #iniciaria en 1
    fila_iniciada=False
    while actual != None:
      if  sentinela_de_filas!=actual.celda.nivel:
        print(sentinela_de_filas,actual.celda.nivel,"hola")
        sentinela_de_filas=actual.celda.nivel
        fila_iniciada=False
        # Cerramos la fila
        text+="""</TR>\n"""  
      if fila_iniciada==False:
        fila_iniciada=True
        #Abrimos la fila
        text+="""<TR>"""  
        text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+actual.celda.prisionero+"""</TD>\n"""
      else:
        text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+actual.celda.prisionero+"""</TD>\n"""
      actual = actual.siguiente
    text+=""" </TR></TABLE>>];
            }
            }\n"""
    f.write(text)
    f.close()
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
    os.system('dot -Tpng Lectura_xml/bb.dot -o Lectura_xml/grafo2.png')
    print("terminado")



  def devolver_cadena_del_grupo(self,grupo):
    string_resultado=""
    string_temporal=""
    buffer=""
    # viene un parametro llamado grupo, es un string con este formato "1,2"
    # recorremos caracter por caracter
    for digito in grupo:
      #si es digito
      if digito.isdigit():
        #añadimos al buffer
        buffer+=digito
      else:
        # si no es buffer, lo vaciamos
        string_temporal=""
        #recorremos la lista y recuperamos los valores para este grupo
        actual = self.primero
        while actual != None:
          # si encontramos coincidencia del digito y el nivel , obtenemos su valor
          if actual.celda.nivel==int(buffer):
            string_temporal+=actual.celda.prisionero+","
          actual = actual.siguiente
        string_resultado+=string_temporal+"\n"
        buffer=""
    #devolvemos el string resultado
    return string_resultado
    