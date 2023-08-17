from nodo_carcel import nodo_carcel

class lista_carceles:
    def __init__(self):
        self.primero=None
        self.contador_carceles=0
    
    def insertar_dato(self,carcel):
        if self.primero is None:
            self.primero=nodo_carcel(carcel=carcel)
            self.contador_carceles+=1
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo_carcel(carcel=carcel)
        self.contador_carceles+=1
    
    def recorrer_e_imprimir_lista(self):
        print("Total de carceles almacenadas:",self.contador_carceles)
        print("")
        print("")
        print("")
        print("******************************************************************")
        actual=self.primero
        while actual != None:
            print("Nombre:",actual.carcel.nombre,"Niveles:",actual.carcel.niveles,
                "Celdas por nivel:",actual.carcel.celdas_por_nivel)
            actual.carcel.lista_celdas.recorrer_e_imprimir_lista()
            actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
            actual=actual.siguiente
            print("")
            print("")
            print("")
        print("******************************************************************")
        print("")
        print("")
        print("")
    

    def grafica_mi_lista_original(self):
        actual=self.primero
        while actual != None:
            actual.carcel.lista_celdas.generar_grafica(actual.carcel.nombre,
                                                    str(actual.carcel.niveles),
                                                    str(actual.carcel.celdas_por_nivel))
            #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
            actual=actual.siguiente

    def grafica_mi_lista_de_patrones(self):
        actual=self.primero
        while actual != None:
            actual.carcel.lista_patrones_celdas.generar_grafica(actual.carcel.nombre,
                                                    str(actual.carcel.niveles),
                                                    str(actual.carcel.celdas_por_nivel))
            #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
            actual=actual.siguiente
         