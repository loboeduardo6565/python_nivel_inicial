ingreso = 0 
nivel0 = 0 # Valor de varible global en el nivel 0

# Es este ejemplo estamos cambiando el valor a la variable global. 
def nuevo_ingreso():
    global ingreso
    ingreso += 1
    print(ingreso)

nuevo_ingreso()

def funcion1():
    nivel1 = 1

    def funcion2():
        global nivel1   # En este caso nivel1 no puede ser invocada como global porq no existe como 
                        # variable global con lo cual solo cambia su valor dentro de nivel 2. 
        nivel1 = 7 
        nivel2 = 2
        print(nivel0, nivel1, nivel2)
    
    funcion2()
    print(nivel0, nivel1)

funcion1()
print(nivel0)