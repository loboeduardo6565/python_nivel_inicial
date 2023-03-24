passw = "qaz123.."
password = input("introduzca su contraseña: ")

consulta = True
while consulta:
    if password == passw:
        print(" \n Ingresando al sistema... \n")
        break
    elif password != passw:
        print("Contraseña incorrecta, por favor intente nuevamente: ")
        password = input("introduzca su contraseña: ")