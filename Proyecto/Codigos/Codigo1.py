import os

# Se llama a la carpeta enfermo_csv.
lista = os.listdir("enfermo_csv")
# print(lista)

# Se llama a la carpeta sano_csv.
lista2 = os.listdir("sano_csv")
# print(lista2)

# Se crea un diccionario para guardar los valores de los animales enfermos.
enfermos = {}

# Se crea un diccionario para guardar los valores de los animales sanos.
sanos = {}

# Recorrer la lista de ganado enfermo.
for i in lista:
    imagen = open("D:/ActividadesdeEstructurasdeDatosyAlgoritmos/enfermo_csv/{i}".format(i=i))
    leer_imagen = imagen.read()
    enfermos[i] = leer_imagen
    # print(enfermos)
    imagen.close()

# Recorrer la lista de ganado sano.
for n in lista2:
    imagen = open("D:/ActividadesdeEstructurasdeDatosyAlgoritmos/sano_csv/{i}".format(i=n))
    leer_imagen = imagen.read()
    sanos[n] = leer_imagen
    print(sanos)
    imagen.close()