"""
Tome dos valores por consola, y guarde en una lista: [primer_valor, segundo_valor, la_suma_de_los_valores] Presente el resultado en la terminal del editor.

"""

primer_valor = int(input("Introduzca un primer valor: ")) # Se asigna el primer valor ingresado por el usuario a la variable "primer_valor" usando la función "int()" para convertir el valor a un entero.
segundo_valor = int(input("Introduzca un segundo valor: ")) # Se asigna el segundo valor ingresado por el usuario a la variable "segundo_valor" de la misma manera que el primer valor.

suma = [primer_valor, segundo_valor, primer_valor + segundo_valor] # Se crea una lista "suma" que contiene los valores de "primer_valor", "segundo_valor" y la suma de ambos.
print(f'La suma del primer valor más el segundo es: {suma[2]}') # Finalmente, se imprime la suma de los dos valores en la consola usando la función "print()" y el formato "f" para incluir el valor de "suma[2]" en la cadena de texto.


