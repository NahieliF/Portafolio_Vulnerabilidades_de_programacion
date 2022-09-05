#Entregable SEP, Portafolio 7.

#Utilizando el loop "for".
nombres = ("Nahieli", "Flores")
for nombre in nombres:
  print (nombre)
#Usando el mismo loop, pero ahora en un diccionario.
canciones = {
  "RHCP" : "Dani California.",
  "Radiohead" : "All I Need.",
  "Pink Floyd": "Keep Talking.",
  "Intoxicados": "De A Ratitos."
}
for canción in canciones:
  print (canciones[canción])

#"Looping" una cadena.
for letra in "Programación":
  print (letra)
#Línea vacía.    
print ()
palabra = "Programar es tedioso"
for letra in palabra :
#Sólo imprime las letras "o" que estén en mi cadena "palabra".
  if letra == "o":
    print (letra)

#Usando un elemento (2) de una lista en una función.
def primero(items):
  print (items[0])
 
números = [2, 7, 9]
primero(números)

#Modificando un elemento (4) de una lista en una función.
def mod(x):
  x[1] = x[1] + 6
  return x
números = [3, 4, 8]
print (mod(números))

#Manipulación de listas en funciones.
n = [4, 6, 8]
def manip(lista):
  lista.append(10)
  return lista
print (manip(n))

#Imprimiendo la lista anterior elemento por elemento en una función.
n = [4, 6, 8]
def imp(x):
  for i in range(0, len(x)):
    print (x[i])

#Modificando cada elemento de una lista en una función.
n = [4, 5, 6]
def multp(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
print (multp(n))

#Usando cadenas en listas en funciones. 
n = ["missing", "björg"]
def uncad(palabras):
  resulta = ""
  for palabra in palabras:
    resulta += palabra
  return resulta

print (uncad(n))

#Usando dos listas como argumentos en funciones.
m = [1, 2, 3]
n = [4, 5, 6]

def lst(x, y):
	return x + y
print (lst(m, n))

#Usando una lista de listas en función.
n = [[8, 7, 6], [5, 4, 3, 2, 1, 0]]
def fnl(listas):
  resultado = []
  for números in listas:
    for número in números:
      resultado.append(número)
  return resultado
print (fnl(n))
