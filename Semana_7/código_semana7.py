#Entregable SEP, portafolio 6.
print ("Nahieli Flores")
#Lista de útiles para la escuela.
mochila = ["cuadernos", "lápiz", "plumones", "celular"]
print (mochila)
#Accediendo a elementos individuales.
print (mochila[0] + " y " + mochila[3])
#Cambiando lápiz por labial.
mochila[1] = "labial"
#Añadiendo elementos a la lista.
mochila.append("rímel")
mochila.append("delineador")
print (mochila)
#Imprimiendo una porción de la mochila.
esencial = mochila[0:3]
print (esencial)
#Imprimiendo apartir de un elemento de la lista
más_esencial = mochila[3:]
print (más_esencial)
#Buscando el número que tenga nuestro elemento.
print (mochila.index("rímel"))
#Añadiendo un elemento en cierto lugar de la lista.
mochila.insert(3, "esmalte")
mochila.remove("cuadernos")
print (mochila)

numeritos = [1, 3, 6, 8, 2, 10]
#Usando el loop for.
for number in numeritos:
  print (2 * number)

animales = ["elefante", "perro", "araña", "gato", "delfín", "hormigas"]
#Ordenando alfabéticamente e imprimiéndolos con sort.
animales.sort() 
for animal in animales:
  print (animal)

#Asignando un diccionario con tres pares key.
residentes = {'Julián' : 104, 'Román' : 105, 'Gregorio' : 106}
print (residentes['Julián'])
print (residentes['Román'])
print (residentes['Gregorio'])
#Realizando cambios al diccionario.
residentes['Azael'] = 108
residentes['Pepe'] = 100
residentes['Juan'] = 102

print ("Hay " + str(len(residentes)) + " residentes en el hotel.")
print (residentes)

#Utilizando el comando del y cambinado el número de habitación de Román.
del residentes['Juan']
del residentes['Gregorio']
residentes['Román'] = '200'
print (residentes)
#Añadiendo un nuevo valor con cadena.
residentes['cuartos_disponibles'] = ['102', '101', '103']
print (residentes)
