from tkinter import *
from tkinter.filedialog import askopenfilename
# Un messagebox sirve para mostrar mensajes emergentes
from tkinter import messagebox


# Creacion de la raiz
root = Tk()
# Titulo de la ventana
root.title("Ejemplo interfaz")
# ¿Quieren que su ventana cambie de tamaño?
root.resizable(False,False)
# Diseño al cursor
root.config(cursor="hand2")
# Definir el tamaño
root.geometry("1200x600")
# Color de fondo
root.config(bg="skyblue")
root.config(bd="30")
root.config(relief="groove")


# configuracion botones de la interfaz

#boton archivo de entrada
boton_archivo_entrada=Button(root,text="Archivo de entrada",font=("Comic Sans MS",20),bg="white",fg="black")
# Colocarle posicion
boton_archivo_entrada.grid(row=0, column=0,padx=10)



#boton archivo de salida
boton_archivo_salida=Button(root,text="Archivo de salida",font=("Comic Sans MS",20),bg="white",fg="black")
# Colocarle posicion
boton_archivo_salida.grid(row=0, column=1,padx=10)


#boton datos del estudiante
boton_datos_estudiante=Button(root,text="Datos del estudiante",font=("Comic Sans MS",20),bg="white",fg="black")
# Colocarle posicion
boton_datos_estudiante.grid(row=0, column=2,padx=10)



#boton para salir
boton_salir=Button(root,text="Salir",font=("Comic Sans MS",20),bg="white",fg="black")
# Colocarle posicion
boton_salir.grid(row=0, column=3,padx=10)

# Función que muestra los datos del estudiante
def informacion_estudiante():
  messagebox.showinfo(title="Mi ejemplo interfaz",message="Erwin Vásquez - 202001534")
boton_datos_estudiante.config(command=informacion_estudiante)


# Funcion cargar archivo de entrada
def cargar_archivo_entrada():
  route=askopenfilename()
  archivo=open(route,'r')
  archivo.close()
  # Aqui deberia ir su lógica de como leer el xml y llenar sus listas 
  # Mensajito exitoso
  messagebox.showinfo(title="Mi ejemplo interfaz",message="Archivo de entrada cargado con éxito")
boton_archivo_entrada.config(command=cargar_archivo_entrada)



# Función para salir del sistema
def salir():
  exit()
boton_salir.config(command=salir)


# La ultima instruccion de mi raiz, ejecutará todo lo que este arriba de ella
root.mainloop()