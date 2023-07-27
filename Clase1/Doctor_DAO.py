#Importaciones
from Doctor import Doctor

class Doctor_DAO:
    def __init__(self):
        self.doctores=[]
        self.contador_doctores=0

    #Función que agrega nuevos doctores
    def agregar_nuevo_doctor(self,nombre, edad,especialidad):
        # validamos que no exista un nombre repetido
        for doctor in self.doctores:
            if doctor.nombre==nombre:
                print("Error, nombre repetido en el doctor!")
                return False
        # Creamos el objeto doctor
        nuevo_doctor=Doctor(self.contador_doctores,nombre,edad,especialidad)
        #Agregamos el paciente al array de pacientes
        self.doctores.append(nuevo_doctor)
        self.contador_doctores+=1
        print("Se agregó un doctor!!")
        return True
    
    def visualizar_doctores(self):
        print("")
        print("")
        print("=============================")
        for doctor in self.doctores:
            print("Id:",doctor.id,"Nombre:",doctor.nombre,"Especialidad:",doctor.especialidad)
        print("=============================")

    def devolver_nombre_por_id(self,id):
        #Recorrer la lista
        for doctor in self.doctores:
            # Encontrar una coincidencia
            if doctor.id==id:
                #Devolver el paciente encontrado
                return doctor.nombre
