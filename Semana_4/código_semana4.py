#Entregable SEP, Portafolio 3.
name= "Nahieli " + "Flores"
print (name)
#Comenzaré mostrando ejemplos de los comparadores.
#Equal to
6 == 6
#Not equal to
6 != 9
#Less than 
6 < 28
#Less than or equal to
4 <= 4
#Greater than
6 > 4
#Greater than or equal to
3 >= 3

#Operador 'and'
3 < 6 and 2 < 4 is True
2 < 4 and 6 > 8 is False 
#Operador 'or'
2 < 6 or 4 > 8 is True
2 > 4 or 4 > 6 is False
#Operador not
not 42 > 40 is False

#Usando if y equal to
if 8 < 12:
  print ("Ocho es menor que doce.")
#Usando if y equal to
answer = "los memes izquierdistas son más divertidos"
if answer == "los memes izquierdistas son más divertidos":
  print ("Es cierto, son re cómicos.")

  #Usando if, comparadores y print
def ejemplo_uno():
  if 22 == 22:
    return "primer logro"
#Ahora +else
def ejemplo_dos (): 
  if 2 > 4:
    return "segundo logro"
  else:
    return "no hubo segundo logro :("
print (ejemplo_uno(), "y", ejemplo_dos())
#Usando if, elif, else y print
def ejemplo_tres(respuesta):
  if respuesta > 4:
    return 2
  elif respuesta < 4:
   return -2
  else: 
    return 0
print (ejemplo_tres(5))
print (ejemplo_tres(4))
print (ejemplo_tres(3))
