from estudiante import estudiante
from lista_doble import lista_doble

estudiante1=estudiante(202001534,10,"Estudiante Nuevo","Sistemas")
estudiante2=estudiante(202100000,200,"Estudiante veterano","Sistemas")
estudiante3=estudiante(202200000,100,"Estudiante Encaminado","Química")


manejador_lista_doble=lista_doble()

print("")
print("")
manejador_lista_doble.insertar_modo_pila(estudiante1)
manejador_lista_doble.insertar_modo_pila(estudiante2)
manejador_lista_doble.insertar_modo_pila(estudiante3)
manejador_lista_doble.recorrer()
print("")
print("")
# Buscamos carnet inexistente
manejador_lista_doble.buscar(20700000)
# Este si lo debería de encontrar
manejador_lista_doble.buscar(202001534)

