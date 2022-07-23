#Este tipo de comentarios simbolizados por el gato, te ayuda a crear notaciones para tu código.
#name es nombre en inglés.
name = "Nahieli FLores"
#subject es materia en inglés.
subject = "Vulnerabilidades en la programación"
print ("Print envía el mensaje que desees a la terminal.")
#Puedes crear una cadena de múltiples líneas, sólo tienes que utilizar tres pares de comillas en lugar de un par.
print ("""Existen Python2 y Python3.
La syntax de Python 2 únicamente requiere las comillas,
mientras que la de Python3 requiere que las comillas estén dentro de paréntesis,
así como en este script.""")
print ('Puedes escribir tu cadena con comillas simples o dobles, pero debes usar la misma para iniciarla y terminarla.')
print ("Podemos combinar múltiples cadenas " + "sumándolas.")

#Podemos realizar operaciones aritméticas asignadas a variables.
edad = 9.5 * 2
print (edad)
#O nuestras variables pueden ser nuestras operaciones aritméticas y así ir actualizando sus valores.
manzanas_que_tengo = 20
manzanas_que_se_comió_mi_hermana = 5
manzanas_que_tengo = manzanas_que_tengo - manzanas_que_se_comió_mi_hermana
mi_otra_hermana_se_comió_otras = 3
manzanas_que_tengo = manzanas_que_tengo - mi_otra_hermana_se_comió_otras

print (manzanas_que_tengo)

#Existe una cosa que se llama booleans, que son los que tienen únicamente dos valores, "falso" y "verdadero", que son asignados a una variable.

mi_nombre_es_Juana = False
mi_edad_es_19 = True
#También puede salir el valor booleano desde una expresión.
a = 10
b = 20
print (a == b)

#En la conversión de las variables a otro tipos de datos, también se puede sumar, por ejemplo, cadenas con enteros y hay determinadas funciones para ello.
print ("Yo tengo " + str(edad) + " años.")

print ("""
Funciones:
Convertir un entero como parte de una cadena. “... ” + str(x) + “ ...”.
Convertir cadena en datos numéricos para operaciones aritméticas. Variable = int(x) + int(y).
Convertir una cadena o número entero a un decimal. Print float(x) 
Convertir decimal a número entero. Print int(float)""")
