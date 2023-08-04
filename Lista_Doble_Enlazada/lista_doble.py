# Importaciones
from nodo import nodo

class lista_doble:
    def __init__(self):
        self.primero=None

    def insertar(self,estudiante):
        # Se inicializa un nuevo nodo, que almacenará la información
        nuevo_nodo= nodo(estudiante=estudiante)
        # Verificamos si el primer nodo de la lista es nulo
        if self.primero is None:
            self.primero=nuevo_nodo
        else:
            # Hacemos referencia a la cabeza de nuestra lista
            actual=self.primero
            # Mientras exista actual.siguiente
            while actual.siguiente:
                actual=actual.siguiente
            # Cuando ya no exista un siguiente, encontramos la posición que ocupará el nuevo nodo
            actual.siguiente=nuevo_nodo
            nuevo_nodo.anterior=actual
    
    def insertar_modo_pila (self,estudiante):
        # Verificamos si el primer nodo de la lista es nulo
        if self.primero is None:
            self.primero=nodo(estudiante=estudiante)
        else:
            actual=nodo(estudiante=estudiante,siguiente=self.primero)
            self.primero.anterior=actual
            self.primero=actual

            

    def recorrer(self):
        # Verificamos que la lista no esté vacía
        if self.primero is None:
            print("La lista se encuentra vacía")
            return
        # Hacemos referencia al primero
        actual=self.primero
        # imprimimos los datos
        print("Créditos:",actual.estudiante.creditos_aprobados,
                "Nombre:",actual.estudiante.nombre,
                "Carrera",actual.estudiante.carrera)
        # Mientras exista actual.siguiente
        while actual.siguiente:
            # Nos trasladamos al siguiente nodo
            actual=actual.siguiente
            print("Créditos:",actual.estudiante.creditos_aprobados,
                "Nombre:",actual.estudiante.nombre,
                "Carrera",actual.estudiante.carrera)
    
    def buscar(self,carne):
        # Hacemos referencia al primero
        actual=self.primero
        # Mientras exista actual.siguiente
        while actual.siguiente:
            # Nos trasladamos al siguiente nodo
            if actual.estudiante.carne==carne:
                print("Estudiante encontrado con el nombre",actual.estudiante.nombre)
                return
            actual=actual.siguiente
        print("Error, estudiante no encontrado :(")
    

    def insertar_ordenado(self, estudiante):
        nuevo_nodo = nodo(estudiante=estudiante)
        if self.primero is None:
        # Si la lista está vacía, simplemente se inserta el nuevo estudiante como el primero
            self.primero = nuevo_nodo
            return
        # Comparar el creditos_aprobados del nuevo estudiante con el primero de la lista
        if estudiante.creditos_aprobados < self.primero.estudiante.creditos_aprobados:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
            return
        actual = self.primero
        while actual.siguiente and actual.siguiente.estudiante.creditos_aprobados < estudiante.creditos_aprobados:
            actual = actual.siguiente
        # Insertar el nuevo estudiante después del nodo "actual"
        nuevo_nodo.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = nuevo_nodo
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual
        
        

