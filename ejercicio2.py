"""
Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos
"""

import sys

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

a=int(a)
b=int(b)
c=int(c)

print(f'\r\n ¿El número {a} es multiplo de 2?: {a % 2 == 0}')
print(f'\r\n ¿El número {b} es multiplo de 2?: {b % 2 == 0}')
print(f'\r\n ¿El número {c} es multiplo de 2?: {c % 2 == 0}')

