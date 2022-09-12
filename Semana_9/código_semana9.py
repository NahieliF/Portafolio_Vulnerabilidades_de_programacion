print ("Jueguito de Nahieli Flores")
#Portafolio 8.
#Exportando lo necesario.
from random import randint
#Creando el tablero.
board = []
#Creación propia de la cuadrícula.
for x in range(0, 5):
  board.append(["O"] * 5)
#Quitando comillas y comas que se ven feas.
def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#Esto es visible para el jugador, se debe borrar si se presenta a alguien así no le regalamos la respuesta.
print (ship_row)
print (ship_col)

#Creando el loop para la función del juego.
for turn in range(4):
  print ("Turn"), turn + 1
  guess_row = int(input("Adiniva la fila: "))
  guess_col = int(input("Adivina la columna: "))
#Estas serán las respuestas que dará el código después de cada intento del jugador.
  if guess_row == ship_row and guess_col == ship_col:
    print ("¡Felicidades! ¡Hundiste el barco!")
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Uy, eso ni está en el oceano.")
    elif board[guess_row][guess_col] == "X":
      print( "Ya intentaste con esa." )
    else:
      print ("No encontraste el barco. :/")
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print ("Game Over :(")
    print_board(board)
