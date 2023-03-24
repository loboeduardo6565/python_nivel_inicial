"""Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. 
    Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente y al finalizar la compra retorne el monto total gastado. """

total = 0

p1 = input('Desea agregar algún producto a la cuenta: \r\n')

while (p1.upper() != 'SI') or (p1.upper() != 'NO'):
    print(f'Se debe responder con SI O NO')
    p1 = input('Desea continuar cargando productos: \r\n')
    if p1.upper() == 'SI':
        name = input('Ingrese el nombre del producto: ')
        cantidad = input('Ingrese la cantidad de kilos: ')
        precio = input('Ingrese el precio: ')
        total = total + cantidad * precio
        puntos=1
        break;
    elif p1.upper() == 'NO': 
        print(f'¡La respuesta es incorrecta!')
        puntos=0
        break;