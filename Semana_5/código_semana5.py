#Entregable SEP, Portafolio 4.
print ("Nahieli Flores")

#If y elif con grade_converter.
def grade_converter(grade):
  if grade >= 90:
    return "A"
  elif grade >= 80:
    return "B"
  elif grade >= 70:
	  return "C"
  elif grade >= 65:
	  return "D"
  else:
	  return "F"

#Esto debería imprimir una A.
print (grade_converter(92))
#Esto debería imprimir una C.
print (grade_converter(70))
#Esto debería imprimir una F.
print (grade_converter(61))

#Usando input.
ejemplo= input("¿Cómo te llamas? ")
#Esto lo imprime y debemos escribir en la consola la respuesta.
#Ahora asegurándonos de que realmente hay carácteres en la respuesta y que sean letras.
ejemplo_2 = input ("Escribe algo: ")
if len(ejemplo_2) > 0 and ejemplo_2.isalpha():
  print (ejemplo_2)
else:
  print ("vacío")
pyg = 'ay'

#Ahora practicaré para poder usar el Pig Latin.
print ("Pig Latin")

original = input("Escribe una palabra: ")

if len(original) > 0 and original.isalpha():
#Para simplificarlo, lo regresaremos en minúsculas.
  word = original.lower()
#Esto almacenará la primera letra de la palabra que ingresamos.
  first = word[0]
#Con la primera letra almacenada, necesitamos agregar la letra y la cadena de pyg a la cadena original.
  new_word = word + first + pyg
#Esto es para acceder a una porción de la palabra.
  new_word = new_word[1:len(new_word)]
  print (new_word + ", yey, lo logré")
else:
    print ("empty")
