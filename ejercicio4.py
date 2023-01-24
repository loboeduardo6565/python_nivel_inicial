"""Escriba un programa que solicite el radio de una circunferencia y permita calcular el
área. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
𝐴 = 𝜋. 𝑟ଶ
A = Área
π = Número pi igual a 3.1416
r = Radio
"""

print('\r\n El siguiente programa calcula el Área de una circunferencia a partir de su radio \r\n')
r = int(input('Introduzca el radio de la circunferencia: '))
PI= float(3.1416)
A = PI * int(r)**2
print(f'El Área de la circunferencia es: {A}')