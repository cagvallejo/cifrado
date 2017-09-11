# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:14:01 2017

@author: vallejo
"""

import string

from carga_fichero import carga_palabras


nombreFichero = "es.dic"
noCaracteres = " 1234567890¡¿!@#$%^&*()-_+={}[]|\:;·'<>?,./\""
listaPalabras = carga_palabras(nombreFichero)
diccionario = set(listaPalabras)


def es_palabra_valida(dicionario, palabra):
    palabra = palabra.lower()
    palabra = palabra.strip(noCaracteres)
    return palabra in diccionario


minusculas = string.ascii_lowercase + "ñáéíóúü"
mayusculas = minusculas.upper()
totalLetras = len(minusculas)
# print(mayusculas)


def desplaza(letra, desplazamiento):
    res = letra
    if letra in minusculas:
        i = minusculas.index(letra)
        n = (i + desplazamiento) % totalLetras
        res = minusculas[n]
    if letra in mayusculas:
        i = mayusculas.index(letra)
        n = (i + desplazamiento) % totalLetras
        res = mayusculas[n]
    return res


def cifra(texto, desplazamiento):
    res = ''
    for letra in texto:
        res = res + desplaza(letra, desplazamiento)
    return res


texto = "¡Hola, Mundo!"
desplazamiento = 5
textoCifrado = cifra(texto, desplazamiento)
print(textoCifrado)
# cy = 0
# for x in listaPalabras:
#    if "lli" in x or "yi" in x:
#        print(x)
#        cy += 1
# print(cy)

contErpet = 0
for x in listaPalabras:
    if "erpet" in x:
        print(x)
        contErpet += 1
print(contErpet)
