class Sokoban:
  """
  Definimos los componentes

  2 - Cajas
  3 - Paredes
  0 - Muñeco
  1 - Camino
  4 - Metas
  5 - Muñeco_meta
  6 - Caja_meta

  Reglas validas para moverse (Arriba, Derecha, Abajo, Izquierda)

  00 - Muñeco, camino -> [0,1] -> [1,0]
  01 - Muñeco, camino
  02 - Muñeco, caja, camino
  03 - Muñeco, caja, meta
  04 - Muñeco, caja_meta, camino
  05 - Muñeco, caja_meta, meta

  06 - Muñeco_meta, camino
  07 - Muñeco_meta, camino
  08 - Muñeco_meta, caja, camino
  09 - Muñeco_meta, caja, meta
  10 - Muñeco_meta, caja_meta, camino
  11 - Muñeco_meta, caja_meta, meta

  Derecha -> muneco_columna + 1
  Izquierda -> muneco_columna -1
  Abajo -> muneco_fila + 1
  Arriba -> muneco_fila - 1

  """
  mapa = [
      [1,1,1,1,1,1,1,1,1],
      [1,2,3,3,3,3,3,3,1],
      [1,3,3,3,3,3,3,3,1],
      [1,3,3,3,3,3,3,3,1],
      [1,3,3,3,3,3,3,3,1],
      [1,1,1,1,1,1,1,1,1],    
  ]

  #Posicion inicial del muñeco en el mapa
  muneco_fila = 1
  muneco_columna = 1

  def imprimirMapa(self):
    """Imprime el mapa completo
    """
    for fila in self.mapa:
        print(fila)

  def moverDerecha(self):
    """Controla el movimiento del muñeco a la derecha
    """
    #00 - Muñeco, camino -> [2,3] -> [3,2]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 3:
      self.mapa[self.muneco_fila][self.muneco_columna] = 3
      self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
      self.muneco_columna += 1

  def moverAbajo(self):
    """Controla el movimiento del muñeco hacia abajo
    00 -> [3]
    [2] -> [3]
    [3] -> [2]
    """
    if self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 3:
      self.mapa[self.muneco_fila][self.muneco_columna] = 3
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 2
      self.muneco_fila += 1

  def jugar(self):
    """Controla el flujo del juego
    """
    while True:
      self.imprimirMapa()
      opciones = "d-derecha, s-abajo"
      print(opciones)
      movimiento = input("Mover a: ")
      if movimiento == "d":
        self.moverDerecha()
      elif movimiento == "s":
        self.moverAbajo()
      elif movimiento == "q":
        break

juego = Sokoban()
juego.jugar()

#00 - Personaje, espacio -> [0,1] -> [1,0]
if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 1:
            self.mapa[self.muneco_fila][self.muneco_columna] = 1
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0
            self.muneco_columna += 1
      
    #01 - Personaje, meta -> [0,4] -> [1,5]        
elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 1
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
            self.muneco_columna += 1

      #04 - Muñeco, caja, espacio [0, 2, 1] -> [1, 0, 2]
elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 1:
           self.mapa[self.muneco_fila][self.muneco_columna] = 1
           self.mapa[self.muneco_fila][self.muneco_columna +1] = 0
           self.mapa[self.muneco_fila][self.muneco_columna +2] = 2
           self.muneco_columna += 1 

      #05 - Muñeco, caja, meta [0,2,4] -> [4,0,2]
elif self.mapa[self.muneco_fila][self.muneco_columna] ==0 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna]= 1
            self.mapa[self.muneco_fila][self.muneco_columna +1] = 0
            self.mapa[self.muneco_fila][self.muneco_columna +2] = 2
            self.muneco_columna += 1 
  





   


