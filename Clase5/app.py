import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from carcel import carcel
from lista_celdas import lista_celdas
from lista_carceles import lista_carceles
from lista_patrones import lista_patrones
from lista_grupos import lista_grupos
from celda import celda
# Definir el XML
lista_senales=[]

route = askopenfilename()
archive = open(route,"r")
archive.close()
# Parsear el XML
tree = ET.parse(route)
root = tree.getroot()


# Recorrer las señales y datos e imprimir atributos y valores
lista_carceles_temporal=lista_carceles()
for carcel_temporal in root.findall('carcel'):
    nombre_carcel = carcel_temporal.get('nombre')
    niveles_carcel = carcel_temporal.get('nivel')
    celdas_por_nivel = carcel_temporal.get('numeroCelda')
    lista_celdas_temporal = lista_celdas()
    lista_celdas_patrones_temporal=lista_celdas()
    # Nuestras 2 listas nuevas, una para patrones y otra para los grupos
    lista_patrones_temporal=lista_patrones()
    lista_grupos_temporal=lista_grupos()
    for celda_carcel in carcel_temporal.findall('celda'):
        nivel_celda = celda_carcel.get('nivel')
        numero_celda = celda_carcel.get('numeroCelda')
        prisionero_celda = celda_carcel.text
        nuevo=celda(int(nivel_celda),int(numero_celda),prisionero_celda)
        lista_celdas_temporal.insertar_dato_ordenado(nuevo)
        # Inserción en mi lista de patrones celda:
        if prisionero_celda!="NULL":
            nuevo=celda(int(nivel_celda),int(numero_celda),1)
            lista_celdas_patrones_temporal.insertar_dato_ordenado(nuevo)
        else:
            nuevo=celda(int(nivel_celda),int(numero_celda),0)
            lista_celdas_patrones_temporal.insertar_dato_ordenado(nuevo)
    lista_carceles_temporal.insertar_dato(carcel(nombre_carcel,niveles_carcel,celdas_por_nivel,lista_celdas_temporal,lista_celdas_patrones_temporal,lista_patrones_temporal,lista_grupos_temporal))
# calculamos los patrones de esta carcel "Carcel De Seguridad"
lista_carceles_temporal.recorrer_e_imprimir_lista()
lista_carceles_temporal.calcular_los_patrones("Carcel De Seguridad")









