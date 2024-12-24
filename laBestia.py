import random

#Definimos las variables que vamos a utlizar
#Esta variable guarda las habitaciones que hay en la casa
rooms = ("Dormitorio", "Baño", "Sala de Estar", "Cocina", "Sotano")

actual_room = 0

#Los posibles Items que puedes encontrar
items = ("Reloj de cuerda","Lata", "Bateria")

#Tu inventario
inventary = ["linterna"]

#Personaje
caracter ={
    "nombre" : "Sofia",
    "inventario" : inventary,
    "room" : actual_room
}

#Le asignamos un nombre al personaje
def create_caracter(nombre):
    caracter["nombre"] = nombre

# Aumentamos y disminuimos el inventario
def aumemtar_inventario(item):
    inventary.append(item)
    caracter[inventary] = inventary

def aumemtar_inventario(item):
    del inventary[item]
    caracter[inventary] = inventary


#REG means Random Event Generator
def REG (range_init, range_end):
    REG = random.randint(range_init, range_end+1)
