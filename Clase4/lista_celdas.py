from nodo_celda import nodo_celda
import sys
import os

class lista_celdas:
    def __init__(self):
        self.primero=None
        self.contador_celdas=0

    def insertar_dato(self,celda):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero=nodo_celda(celda=celda)
            self.contador_celdas+=1
            return
        #Temporal para recorrer nuestra lista
        actual=self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo_celda(celda=celda)
        self.contador_celdas+=1
    

    def recorrer_e_imprimir_lista(self):
        print("============================================================")
        actual=self.primero
        while actual !=None:
            print("Nivel:",actual.celda.nivel,"No. celda:",actual.celda.numero_celda,
                "Prisionero:",actual.celda.prisionero)
            actual=actual.siguiente
        print("============================================================")


    def generar_grafica(self,nombre_carcel,niveles,celdas_por_nivel):
        f = open('bb.dot','w')
        # configuraciones del grafo
        text ="""
            digraph G {"niveles="""+niveles+"""","CeldasNivel="""+celdas_por_nivel+""""->" """+nombre_carcel+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.celda.nivel #iniciaria en 1
        fila_iniciada=False
        while actual != None:
            # Si mi fila actual es diferente a la que viene
            if  sentinela_de_filas!=actual.celda.nivel:
                #print(sentinela_de_filas,actual.celda.nivel,"hola")
                sentinela_de_filas=actual.celda.nivel
                fila_iniciada=False
                # Cerramos la fila
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                #Abrimos la fila
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.celda.prisionero)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.celda.prisionero)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o 17agosto.png')
        print("terminado")




    