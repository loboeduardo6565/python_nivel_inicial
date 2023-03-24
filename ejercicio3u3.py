"""Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas 
    veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.  """

oracion = input("Ingrese una oración")

contador = 0

for letras in oracion:
    if letras == "Á":
        contador += 1
        print(f"La letra a aparece en la oración {contador} veces")
    if letras == "a" or letras == "á" or letras =="A":
        contador += 1
        print(f"La letra a aparece en la oración {contador} veces")