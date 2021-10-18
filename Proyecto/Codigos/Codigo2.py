import numpy as np
import os
from numpy import genfromtxt
from matplotlib import pyplot as plt

def interpolacionKNN(img,dstH,dstW):
    scrH,scrW=img.shape
    retimg=np.zeros((dstH,dstW),dtype=np.uint8)
    for i in range(dstH):    
        for j in range(dstW):
            scrx=round((i+1)*(scrH/dstH))
            scry=round((j+1)*(scrW/dstW))
            retimg[i,j]=img[scrx-1,scry-1]
    return retimg

lista = os.listdir("D:/ActividadesdeEstructurasdeDatosyAlgoritmos/enfermo_csv/")

for i in lista:
    # Imagen original
    print()
    image = np.genfromtxt("D:/ActividadesdeEstructurasdeDatosyAlgoritmos/enfermo_csv/{i}".format(i=i), delimiter=",")
    # print("El tamaño de la matriz es de " + str(image.nbytes) + " bytes.") Esto es para ver que tasa de compresión tiene el KNN.
    print("Matriz de la imagen " + str(i))
    print()
    print(image)
    imgplot = plt.imshow(image, cmap='gray') #Setea la imagen que se mostrara
    plt.show() #Mostrará la imagen

    print()

    # Imagen Comprimida con KNN
    imagenComprimida = interpolacionKNN(image, image.shape[0]*2 , image.shape[1]*2)
    # print("El tamaño de la matriz comprimida es de " + str(imagenComprimida.nbytes) + " bytes.") Esto es para ver que tasa de compresión tiene el KNN.
    print("Matriz de la imagen comprimida " + str(i))
    print()
    print(imagenComprimida)
    imgplot2 = plt.imshow(imagenComprimida, cmap='gray') #Setea la imagen que se mostrara
    plt.show() #Mostrará la imagen

lista2 = os.listdir("D:/ActividadesdeEstructurasdeDatosyAlgoritmos/sano_csv")

for n in lista2:
    print()
    image = np.genfromtxt("D:/ActividadesdeEstructurasdeDatosyAlgoritmos/sano_csv{i}".format(i=n), delimiter=",")
    # print("El tamaño de la matriz es de " + str(image.nbytes) + " bytes.") Esto es para ver que tasa de compresión tiene el KNN.
    print(image)
    imgplot = plt.imshow(image, cmap='gray') #Setea la imagen que se mostrara
    plt.show() #Mostrará la imagen

    print()

    # Imagen Comprimida con KNN
    imagenComprimida2 = interpolacionKNN(image, image.shape[0]*2 , image.shape[1]*2)
    # print("El tamaño de la matriz comprimida es de " + str(imagenComprimida2.nbytes) + " bytes.") Esto es para ver que tasa de compresión tiene el KNN.
    print("Matriz de la imagen comprimida " + str(n))
    print()
    print(imagenComprimida2)
    imgplot2 = plt.imshow(imagenComprimida2, cmap='gray') #Setea la imagen que se mostrara
    plt.show() #Mostrará la imagen