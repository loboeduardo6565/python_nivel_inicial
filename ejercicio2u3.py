"""Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”. """

oracion = input("Ingrese una oración")

contador = 0

for letras in oracion:
    if letras == "a":
        contador += 1
        print(f"La letra a aparece en la oración {contador} veces")

