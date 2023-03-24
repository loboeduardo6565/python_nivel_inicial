variable1 = 6 # Como esta variable está definida en la raiz del archivo, en la parte superior, es una variable global. 

# Función, bloque, rutina: Fuera del bloque no puedo acceder a una variable a menos de que la retorne
def sumar_cinco(b):
    c = variable1 + b # Mientras que c es una variable local. 
    return c # Permite retornar un valor 

print(sumar_cinco(5))

