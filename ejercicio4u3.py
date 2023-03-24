""" Escriba un programa que solicite la edad de la 
    persona e imprima todos los años que la persona ha cumplido. """

edad = input("Ingrese su edad: ")
edad = int(edad)

for anios in range(edad +1):
    if anios == 1: 
        print(f"Ud ha cumplido {anios} año")
    if anios >1:
        print(f"Ud ha cumplido {anios} años")