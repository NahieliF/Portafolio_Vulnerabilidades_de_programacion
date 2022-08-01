#Esto es parte del Entregable SEP. Portafolio 2.
name = "Nahieli Flores"
#Mi nombre sigue siendo el mismo.
print (name)
#De los caracteres conflictivos, por ejemplo, sería el apostrofe:'There's a vato in my heart'
#El código ahí se rompería, ya que Python cree que el apostrofe es para terminar la cadena. Para solucionarlo sólo debemos poner un slash al revés.
print ('There\'s a vato in my heart')

animales = "gatos"[3]
#El índice aquí sería la "o" de gatos, ya que comienza a contar desde cero.
print (animales)

#Los métodos de cadena que vi son los siguientes: len, lower, upper y str.

nesquik = "Cereal más chocolatoso"
print (len(nesquik))
#len() sirve para contar el número de caracteres de mi cadena.
print (nesquik.lower())
#lower() te regresa la cadena en minúsuculas.
print (nesquik.upper())
#upper() es su contrario, te la regresa en mayúsculas.
pi = 3.141592
print (str(pi))
#str() convierte las no-cadenas en cadenas.

#Utilizando el operador %.
pt1 = "la escuela"
pt2 =  "comprar pastes"
print ('No vayamos a %s. Mejor vayamos a %s.' % (pt1, pt2))

#Utilizando datetime.
from datetime import datetime
#Esto importa la librería de datetime para poder utilizarla.
ahora = datetime.now()
#Esto guarda la fecha actual en la variable "ahora".
print (ahora)
#También se puede imprimir individualmente la fecha.
print (ahora.year)
print (ahora.month)
print (ahora.day)
#O podemos cambiar el formato.
print ("%02d/%02d/%04d" % (ahora.month, ahora.day, ahora.year))
#No sólo se puede con fechas, sino que también con la hora.
print ('%02d:%02d:%02d' % (ahora.hour, ahora.minute, ahora.second))
#O todo junto.
print ('%02d/%02d/%04d %02d:%02d:%02d' % (ahora.month, ahora.day, ahora.year, ahora.hour, ahora.minute, ahora.second))
