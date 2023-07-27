from Paciente_DAO import Paciente_DAO
from Doctor_DAO import Doctor_DAO

#instancias de las clases
manejador_pacientes=Paciente_DAO()
manejador_doctores=Doctor_DAO()


def registrar_paciente():
    print("")
    nombre=input("Ingrese el nombre del paciente: ")
    edad=input("Ingrese la edad del paciente: ")
    manejador_pacientes.agregar_nuevo_paciente(nombre,edad)

def registrar_doctor():
    print("")
    nombre=input("Ingrese el nombre del doctor: ")
    edad=input("Ingrese la edad del doctor: ")
    especialidad=input("Ingrese la especialidad del doctor: ")
    manejador_doctores.agregar_nuevo_doctor(nombre,edad,especialidad)

def ver_los_pacientes():
    manejador_pacientes.visualizar_pacientes()
def ver_los_doctores():
    manejador_doctores.visualizar_doctores()

def agendar_una_cita():
    print("")
    id_paciente=input("Ingrese el id del paciente: ")
    id_doctor=input("Ingrese el id del doctor: ")
    motivo=input("Ingrese el motivo de la cita: ")
    manejador_pacientes.agendar_cita(manejador_pacientes.devolver_nombre_por_id(int(id_paciente)),
                                    manejador_doctores.devolver_nombre_por_id(int(id_doctor)),
                                    motivo)

def mostrar_menu():
    print("")
    print("")
    print("-------Menú-----------")
    print("1. Registrar Paciente")
    print("2. Registrar Doctor")
    print("3. Ver pacientes en el sistema")
    print("4. Ver doctores en el sistema")
    print("5. Agendar Cita")
    print("6. salir")
    opcion=input("Ingrese una opción del menú: ")
    while True:
        if opcion=="1":
            registrar_paciente()
        elif opcion=="2":
            registrar_doctor()
        elif opcion=="3":
            ver_los_pacientes()
        elif opcion=="4":
            ver_los_doctores()
        elif opcion=="5":
            agendar_una_cita()
        elif opcion=="6":
            print("Saliendo del programa, vuevla pronto")
            break
        else:
            print("Indique una opción válida")
        mostrar_menu()
            

mostrar_menu()




