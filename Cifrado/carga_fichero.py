# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:06:01 2017

@author: vallejo
"""

# DO NOT MODIFY THIS FUNCTION ###


def carga_palabras(nombreFichero):
    '''
    nombreFichero (string): el nombre del fichero con las palabras que cargar

    Returns: una lista de palabras válidas. Las palabras son String en minúculas

    Dependiendo del tamaño de la lista de palabras,
    esta función puede tardar un poco
    '''
#    print('Loading word list from file...')
    print('Cargando lista de palabras del fichero...')
    # ficheroEntrada: fichero
    ficheroEntrada = open(nombreFichero, 'r')
    # linea: string
    listaPalabras = ficheroEntrada.readlines()
    # Para quitar los saltos de línea finales y pasar a minúsculas;
    # las palabras en el fichero original están ya en minúsculas, pero por si:
    listaPalabras = [x.strip().lower() for x in listaPalabras]
    # listaPalabras: lista de strings
    print('  ', len(listaPalabras), 'palabras cargadas.')
    ficheroEntrada.close()

    return listaPalabras


# listaPalabras = carga_palabras(nombreFichero)
# print(listaPalabras)
