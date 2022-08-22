#Entregable SEP, Portafolio 5.
name = "Nahieli Flores"
print (name)

#Ejemplo de una función simple.
def ejemplo(n):
  """Regresa el cuadrado de un número."""
  cuadrado = n ** 2
  print (("%d al cuadrado es %d.") % (n, cuadrado))
  return cuadrado
ejemplo(10)
#Ejemplo de una función llamando a otra función. 
def merece_uno(n):
  return n + 1
def merece_otro(n):
  return merece_uno(n) + 2

#Importación genética con el módulo math.
import math
print (math.sqrt(25))
#Si no hubiera importado, la operación no habría sido posible, ya que daría un SyntaxError.

#Importación de funciones, importando todo del módulo.
from math import *
everything = dir(math)
#Imprimiendo todo lo que esté disponible en el módulo math.
print (everything)

#Usando max.
máximo = max(4, 6, 8)
print (máximo)
#Usando min.
mínimo = min(2, 6, 8)
print (mínimo)

#Imprimiendo los tipos de un int, float y str.
print (type(108))
print (type(3.14))
print (type('hola'))

#Ejemplo de planeación de viaje con lo visto en este entregable. 
def costo_hotel(noches):
  return 140 * noches

def viaje_avion(ciudad):
  if ciudad == "Buenos Aires":
    return 600
  elif ciudad == "Berlín":
    return 400
  elif ciudad == "Durango":
    return 300
  elif ciudad == "Alcorcón":
    return 200

def renta_carro(días):
  costo = días * 40
  if días >= 7:
    costo -= 50
  elif días >= 3:
    costo -= 20
  return costo

def costo_viaje(ciudad, días, gastos_de_dinero):
  return renta_carro(días) + costo_hotel(días) + viaje_avion(ciudad) + gastos_de_dinero

print (costo_viaje("Buenos Aires", 5, 600))
