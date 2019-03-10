import json

def Lista (doc):
    listaN = []
    listaD = []):
    for alquiler in doc ["directorios"]["directorio"]:
        listaN.append (alquiler["nombre"]["content"])
    for direcciones in doc ["directorios"]["directorio"]:
        listaD.append (direcciones["direccion"][1]["content"])
    return zip (listaN,listaD)

def Contar (doc):
    lista = []
    lista1= []
    for datos in doc ["directorios"]["directorio"]:
        if (datos["web"] == ""):
            lista1.append (datos ["web"])
        else:
            lista.append (datos ["web"])
            total = len(lista)
    return total

def Filtro (doc):
    for datos in doc ["directorios"]["directorio"]:
        for

with open("alquiler de coches.json") as fichero:
    doc = json.load(fichero)

while True:
    print ('''Menu:
        1. Listar información: Listar nombre de todos los sitios en los que puedan alquilarse coches y su localizacion.
        2. Contar Informacion: Mostrar sitios de alquiler y contar cuantos de ellos cuentan con foto y pagina web.
        3. Buscar o filtrar: Mostrar sitios en los que se pueda alquilar coches para congresos.
        4. Busqueda relacionada: Pedir por teclado un horario y mostrar que sitios estan abiertos.
        5. Ejercicio libre: Mostrar localizacion de los sitios de alquiler usando tanto las coordenadas como openstreetmap.
        0. Salir
        ''')

    opcion = input("opcion: ")

    if opcion == "1":
        for listaN ,listaD in Lista (doc):
            print ("*",listaN,"-",listaD)

    elif opcion == "2":
        print (Contar (doc))

    elif opcion == "0":
        break;

    else:
        print ("ERROR, esa opcion no existe")
