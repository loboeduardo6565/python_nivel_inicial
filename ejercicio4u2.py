""" Realice un programa que consulte la edad y en caso de que el valor ingresado supere la
    fecha de jubilación, presente en la terminal el mensaje “Ya está en edad de jubilarse" en 
    caso contrario que presente Aún está en edad de trabajar”

"""
EDAD_JU=65 # Cambie la fecha de jubilación según desee
EDAD_JU = int(EDAD_JU)
edad = int(input("Introduzca su edad: "))

if edad < 18:
    print("Usted no tiene edad para trabajar")
elif edad > 18 and edad >= EDAD_JU:
    print("Ya está en edad de jubilarse")
else:
    print("Aún está en edad de trabajar")

