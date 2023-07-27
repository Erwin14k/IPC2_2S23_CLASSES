#Importaciones
from Paciente import Paciente

class Paciente_DAO:
    def __init__(self):
        self.pacientes=[]
        self.contador_pacientes=0

    #Función que agrega nuevos pacientes
    def agregar_nuevo_paciente(self,nombre, edad):
        # validamos que no exista un nombre repetido
        for paciente in self.pacientes:
            if paciente.nombre==nombre:
                print("Error, nombre repetido en el paciente!")
                return False
        # Creamos el objeto paciente
        nuevo_paciente=Paciente(self.contador_pacientes,nombre,edad)
        #Agregamos el paciente al array de pacientes
        self.pacientes.append(nuevo_paciente)
        self.contador_pacientes+=1
        print("Se agregó un paciente!!")
        return True
    
    def visualizar_pacientes(self):
        print("")
        print("")
        print("=============================")
        for paciente in self.pacientes:
            print("Id:",paciente.id,"Nombre:",paciente.nombre)
        print("=============================")
    
    def devolver_nombre_por_id(self,id):
        #Recorrer la lista
        for paciente in self.pacientes:
            # Encontrar una coincidencia
            if paciente.id==id:
                #Devolver el paciente encontrado
                return paciente.nombre
    
    def agendar_cita(self,paciente,doctor,motivo):
        print("Se agendó una cita para el paciente:",paciente,
                "Por el motivo de:",motivo, 
                "Y será atendida por el doctor:",doctor)

            