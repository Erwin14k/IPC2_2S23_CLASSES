
# Importaciones
from Semestre_DAO import Semestre_DAO
from Curso import Curso

#Manejadores (Instancia de la clase)
semestre_handler=Semestre_DAO()


# Insierción de semestres, Todo bien
semestre_handler.agregar_nuevo_semestre(1,"Primer Semestre")
semestre_handler.agregar_nuevo_semestre(2,"Segundo Semestre")
semestre_handler.agregar_nuevo_semestre(3,"Tercer Semestre")
semestre_handler.agregar_nuevo_semestre(4,"Cuarto Semestre")
# Error, el numero del semestre ya existe
semestre_handler.agregar_nuevo_semestre(1,"Primer Semestre")

# Insierción de cursos
semestre_handler.agregar_nuevo_curso_al_semestre(4,Curso("0771","Ipc2",6))
semestre_handler.agregar_nuevo_curso_al_semestre(4,Curso("0779","Lenguajes formales",6))
semestre_handler.agregar_nuevo_curso_al_semestre(3,Curso("0770","Ipc1",6))
semestre_handler.agregar_nuevo_curso_al_semestre(1,Curso("0001","Idioma ténico 1",2))
#Error semestre no encontrado
semestre_handler.agregar_nuevo_curso_al_semestre(10,Curso("0001","No se debe agregar",2))

# ver información recolectada
semestre_handler.imprimir_información_semestres()

