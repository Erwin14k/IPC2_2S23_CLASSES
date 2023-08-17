# Importaciones
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from carcel import carcel
from lista_carceles import lista_carceles
from lista_celdas import lista_celdas
from celda import celda

# Recuperar el xml
ruta =askopenfilename()
archivo= open(ruta,"r")
archivo.close()

# Parsear para que nuestra aplicación entienda que manipulará xml
tree = ET.parse(ruta)
raiz=tree.getroot()

#Lectura del xml
# Definimos mi lista que guarde todas las carceles
lista_carceles_temporal=lista_carceles()
for carcel_temporal in raiz.findall('carcel'):
    # Obtener atributos principales (nombre, niveles, celdas_por_nivel)
    nombre_carcel=carcel_temporal.get('nombre')
    niveles_carcel=carcel_temporal.get('nivel')
    celdas_por_nivel=carcel_temporal.get('numeroCelda')
    # Inicializamos nuestras listas
    lista_celdas_temporal=lista_celdas()
    lista_celdas_patrones_temporal=lista_celdas()
    for celda_carcel in carcel_temporal.findall('celda'):
        nivel_celda=celda_carcel.get('nivel')
        numero_celda=celda_carcel.get('numeroCelda')
        prisionero_celda=celda_carcel.text
        nuevo=celda(int(nivel_celda),int(numero_celda),prisionero_celda)
        lista_celdas_temporal.insertar_dato(nuevo)
        # Inserción en lista de patrones celda
        if prisionero_celda !="NULL":
            nuevo=celda(int(nivel_celda),int(numero_celda),1)
            lista_celdas_patrones_temporal.insertar_dato(nuevo)
        else:
            nuevo=celda(int(nivel_celda),int(numero_celda),0)
            lista_celdas_patrones_temporal.insertar_dato(nuevo)
    lista_carceles_temporal.insertar_dato(carcel(nombre_carcel,niveles_carcel,celdas_por_nivel,
                                                lista_celdas_temporal,lista_celdas_patrones_temporal))
lista_carceles_temporal.recorrer_e_imprimir_lista()
lista_carceles_temporal.grafica_mi_lista_de_patrones()

