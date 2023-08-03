#Importación de clase semestre
from Semestre import Semestre

class Semestre_DAO:
    def __init__(self):
        self.semestres=[]
        #(1,semestr1,[mate1,social1]), (1,semestr1,[mate1,social1])


    # Función para agregar un nuevo semestre
    def agregar_nuevo_semestre(self,numero_semestre,nombre):
        for semestre in self.semestres:
            # Validar que el numero de semestre no exista, en caso existir, acabar con la ejecución
            if semestre.numero_semestre==numero_semestre:
                print("Error, el número del semestre ya existe")
                return False
        # Creamos el nuevo semestre
        nuevo_semestre = Semestre(numero_semestre,nombre,[])
        #Agregamos el nuevo semestre
        self.semestres.append(nuevo_semestre)
        print("Se creó satisfacotariamente el semestre",numero_semestre)
    
    
    # Función para agregar un nuevo curso al semestre
    def agregar_nuevo_curso_al_semestre(self,numero_semestre,curso):
        for semestre in self.semestres:
            #Intentamos encontrar el semestre 
            if semestre.numero_semestre==numero_semestre:
                semestre.cursos.append(curso)
                print("Se agregó el curso",curso.nombre,"Al semestre",semestre.numero_semestre)
                return True
        print("Error, el semestre",numero_semestre,"no existe :(")

    # Procedimiento para imprimir toda la información recolectada
    def imprimir_información_semestres(self):
        for semestre in self.semestres:
            print("=============================")
            print("Semestre No.",semestre.numero_semestre)
            for curso in semestre.cursos:
                print("---",curso.nombre)
            print("============================")




