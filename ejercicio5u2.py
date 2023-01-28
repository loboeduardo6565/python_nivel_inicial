""" Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de utilizar una
    función, de forma que la operación se realice dentro de la misma
"""

"""
    Ejercicio 3
    """
def perimetro(r):
    print('\r\n Función que calcula el perímetro de una circunferencia a partir de su radio \r\n')
    PI= float(3.1416)
    L = 2 * (int(r) * PI)
    print(f'El perímetro de la circunferencia es: {L}')

perimetro(5)

"""
    Ejercicio 4
    """
def area(r):
    print('\r\n Función que calcula el Área de una circunferencia a partir de su radio \r\n')
    PI= float(3.1416)
    A = PI * int(r)**2
    print(f'El Área de la circunferencia es: {A} \r\n')

area(6)

"""
    Ejercicio 5
    """
def incremento(diez):
    porcentaje = 10 * diez / 100
    print(f"El número se incrementó en 10% quedando en: {porcentaje+diez} \r\n")

incremento(100) # El número enviado como parametrp seráincrementado en 10%