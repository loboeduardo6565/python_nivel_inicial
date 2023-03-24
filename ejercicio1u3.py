""" Tome el ejercicio de cálculo de números pares e impares de la unidad 2 y agréguele un bucle al código de forma de simplificarlo. """

import sys

a = int(sys.argv[1]) 
b = int(sys.argv[2])
c = int(sys.argv[3])

lista = [a,b,c]

for i in lista:
    if i % 2 == 0:
        print(f'\r\n El número {i} Es multiplo de 2 ')
    else: 
        print(f'\r\n El número {i} No es multiplo de 2 ')




