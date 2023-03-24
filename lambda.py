# Función normal 

def normal(a, b):
    c = a + b
    return c

print(normal(2, 4))


# Función Lambda: Se define en la misma línea en la cual se usa

b = lambda a,b: a + b
print (b(2,4))

numero = lambda num: num % 2 != 0 # Se define en la misma línea en la cual se usa
print (numero(2))
print (numero(3))

# Otro ejemplo de función lambda

suma = lambda x,y: x + y
print(suma(3,3))

# Otro ejemplo de función lambda

revertir = lambda cadena: cadena[::-1] 
print(revertir("Python"))

# Otro ejemplo de función lambda

doblar = lambda numero: numero * 2
print(doblar(5))