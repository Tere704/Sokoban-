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
  07 - Muñeco_meta, meta
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
    for fila in self:
    #for fila in self.mapa:
      print(fila)

  def moverDerecha(self): #verificar qué es una fila __ y qué es una columna | y cambiar la dirección (Abajo) :-\
    """Controla el movimiento del muñeco a la derecha
    """
    #00 - Muñeco, camino -> [0,1] -> [1,0]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 1:
     self.mapa[self.muneco_fila][self.muneco_columna] = 1
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0
     self.muneco_columna += 1
      #Muñeco, meta 
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0  and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 4:
     self.mapa[self.muneco_fila][self.muneco_columna] = 1 
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0 
     self.muneco_columna += 1
      
    #02 - Muñeco, caja, camino  
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 2:
     self.mapa[self.muneco_fila][self.muneco_columna] = 1
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0
     self.mapa[self.muneco_fila][self.muneco_columna + 2] = 2
     self.muneco_columna += 1
    #03 - Muñeco, caja, meta
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 2:
     self.mapa[self.muneco_fila][self.muneco_columna] = 1
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0
     self.mapa[self.muneco_fila][self.muneco_columna + 2] = 6
     self.muneco_columna += 1
    # 04 - Muñeco, caja_meta, camino
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 6:
     self.mapa[self.muneco_fila][self.muneco_columna] = 1
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
     self.mapa[self.muneco_fila][self.muneco_columna + 2] = 2
     self.muneco_columna += 1
    #05 - Muñeco, caja_meta, meta
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 6:
     self.mapa[self.muneco_fila][self.muneco_columna] = 1
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
     self.mapa[self.muneco_fila][self.muneco_columna + 2] = 6
     self.muneco_columna += 1
    #06 - Muñeco_meta, camino
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5  and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 1:
     self.mapa[self.muneco_fila][self.muneco_columna] = 4 
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0 
     self.muneco_columna += 1
     # 07 - Muñeco_meta, meta
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5  and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 4:
     self.mapa[self.muneco_fila][self.muneco_columna] = 4 
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5 
     self.muneco_columna += 1
    #08 - Muñeco_meta, caja, camino
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5  and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 2:
     self.mapa[self.muneco_fila][self.muneco_columna] = 4 
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0 
     self.mapa[self.muneco_fila][self.muneco_columna + 2] = 2
     self.muneco_columna += 1
    #  09 - Muñeco_meta, caja, meta
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5   and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 2:
     self.mapa[self.muneco_fila][self.muneco_columna] = 4 
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0 
     self.mapa[self.muneco_fila][self.muneco_columna + 2] = 6
     self.muneco_columna += 1
    #10 - Muñeco_meta, caja_meta, camino
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5  and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 6:
     self.mapa[self.muneco_fila][self.muneco_columna] = 4 
     self.mapa[self.muneco_fila][self.muneco_columna + 1] =  5
     self.mapa[self.muneco_fila][self.muneco_columna + 2] = 2
     self.muneco_columna += 1
    #11 - Muñeco_meta, caja_meta, meta
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5  and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 6:
     self.mapa[self.muneco_fila][self.muneco_columna] = 4  
     self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5 
     self.mapa[self.muneco_fila][self.muneco_columna + 2] = 6
     self.muneco_columna += 1

  #Terminamos con la función anterior y comenzaremos con otra
  def moverIzquirda(self):
    """Controla el movimiento del muñeco a la izquierda
    """
    #00 - Muñeco, camino -> [1,0] -> [0,1]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 1:
     self.mapa[self.muneco_fila][self.muneco_columna] = 1
     self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0
     self.muneco_columna -= 1

     #Muñeco, meta 
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0  and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 4:
     self.mapa[self.muneco_fila][self.muneco_columna] = 1 
     self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0 
     self.muneco_columna -= 1 

      

    