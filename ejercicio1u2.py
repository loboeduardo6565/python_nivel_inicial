""" Ejercicio 1 (Este es el ejercicio 2 de la unidad 1 pero implementando if/else Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
    pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si son múltiplos de dos. Utilice la estructura if/else 
    """

import sys

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

a=int(a)
b=int(b)
c=int(c)

if a % 2 == 0:
    print(f'\r\n El número {a} Es multiplo de 2 ')
else: 
    print(f'\r\n El número {a} No es multiplo de 2 ')
if b % 2 == 0:
    print(f'\r\n El número {b} Es multiplo de 2 ')
else: 
    print(f'\r\n El número {b} No es multiplo de 2 ')
if c % 2 == 0:
    print(f'\r\n El número {c} Es multiplo de 2 ')
else: 
    print(f'\r\n El número {c} No es multiplo de 2 ')
