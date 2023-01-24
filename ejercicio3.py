"""
Escriba un programa que solicite el radio de una circunferencia y permita calcular 
el perímetro. Presente el resultado en la terminal del editor. 
Utilice la siguiente fórmula:
L = 2 · π · r
L = Longitud de perímetro
π = Número pí igual a 3.1416
r = Radio
"""

print('\r\n El siguiente programa calcula el perímetro de una circunferencia a partir de su radio \r\n')
r = int(input('Introduzca el radio de la circunferencia: '))
PI= float(3.1416)
L = 2 * (int(r) * PI)
print(f'El perímetro de la circunferencia es: {L}')