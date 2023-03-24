

total = 0
identificador = 0
productos = {}



def app():

    opciones()

    consulta = True
    while consulta:
        opcion = input('Seleccione la opción que desee: \r\n')
        opcion = int(opcion)
        #Opciones
        if opcion == 1:
            nombre, cantidad, precio = input("Ingrese el nombre del producto, cantidad y precio separados por espacio: ").split()
            alta_producto(nombre, cantidad, precio)
            opciones() 
            #consulta = False
        elif opcion == 2:  
            id = input("Ingrese el id del producto a borrar: ")
            baja_producto(int(id))
            opciones()
            #consulta = False
        elif opcion == 3:  
            consulta_producto()
            opciones()
            #consulta = False
        elif opcion == 4:  
            id, precio = input("Ingrese el id y nuevo precio separados por espacio: ").split()
            modificar_precio_producto(int(id), int(precio))
            opciones()
            #consulta = False
        elif opcion == 5:  
            print("Saliendo del sistema...")
            consulta = False
        else:
            print('La opción no es válida, intente de nuevo \r\n')
            opciones()


def opciones():
    print('Seleccione la opción que desee: \r\n')
    print('1) Dar de alta un producto')
    print('2) Dar de baja un producto')
    print('3) Listar productos')
    print('4) Modificar un producto de la compra')
    print('5) Salir del sistema \r\n')


def alta_producto(nombre, cantidad, precio):
    global total
    global identificador
    total = total + float(cantidad) * float(precio)
    productos[identificador] = {'Nombre': nombre, 'Cantidad': cantidad, 'Precio': precio}
    identificador+=1
    print(f"Se agregan los siguientes articulos: {productos}")
    print(f"El total es a pagar es: {total}")

def baja_producto(id):
    global productos 
    global total 
    del productos[id]
    total = total - (float(productos[id][cantidad]) * float(productos[id][precio]))
    print(f"Se borra el item {productos[id]}")
    print(f"Quedando los siguientes articulos: {productos}")
    print(f"El total es a pagar es: {total}")

def consulta_producto():
    global productos
    global total
    print(f"Detalle de articulos: {productos}")
    print(f"El total a pagar es: {total}")

def modificar_precio_producto(id, precio):
    global productos
    global total
    sin_mod = float(productos[id]['cantidad']) * float(productos[id]['precio'])
    productos[id]['precio']=precio
    con_mod = float(productos[id]['cantidad']) * float(productos[id]['precio'])
    total = total + con_mod - sin_mod
    print(f"Detalle de articulos: {productos}")
    print(f"El total a pagar es: {total}")




app()






