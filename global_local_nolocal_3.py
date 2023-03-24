nivel0 = 0

def funcion1():
    nivel1 = 1

    def funcion2():
        nonlocal nivel1   # En este caso nivel1 esta siendo invocada como no global pero tampoco como local es decir es una 
                          # que se encuentra en el intermedio, y su valor si puede ser cambiado desde esta función a los demás niveles
        nivel1 = 7 
        nivel2 = 2
        print(nivel0, nivel1, nivel2)
    
    funcion2()
    print(nivel0, nivel1)

funcion1()
print(nivel0)