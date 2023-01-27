

piloto = {'nombre':"Michael", 'apellido':"Schumacher", 'campeonatos': 7, 'equipo':"Mercedes"}
piloto2 = {'name':"Lewis", 'lastname':"Hamilton", 'championships': 7, 'team':"Mercedes"}


# Primera Forma: Funciona
drivers={"Dic1":piloto, "Dic2":piloto2}
print(drivers)

# Segunda Forma: Funciona
piloto.update(piloto2) 
print(piloto)

# Tercera Forma: Funciona
pilotos = {}
pilotos = {**piloto, **piloto2} 
print(pilotos)

# Cuarta Forma: Funciona
pilotos.update( piloto | piloto2 )
print( pilotos )

""" Cuarta Forma: No funciona
pilotos = {}
pilotos = piloto | piloto2 
"""



"""
print(piloto["nombre"])
print(piloto.get("Schumacher")) # Otra forma de imprimir un valor dentro de un diccionario
print(piloto.keys()) # Imprimiendo las claves dentro de un diccionario
print(piloto.values()) # Imprimiendo los valores dentro de un diccionario
print(piloto.items()) # Imprimiendo de los objetos dentro de un diccionario
print(list(piloto.items())[0])  #Imprimiendo primer item
"""