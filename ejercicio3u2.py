"""
Tome dos valores por consola, y guarde en una lista: [primer_valor, segundo_valor, la_suma_de_los_valores] Presente el resultado en la terminal del editor.

"""

primer_valor = int(input("Introduzca un primer valor: "))
segundo_valor = int(input("Introduzca un segundo valor: "))

suma = [primer_valor, segundo_valor, primer_valor + segundo_valor]
print(f'La suma del primer valor más el segundo es: {suma[2]}')