from src.tablero import Tablero
from src.jugador import Jugador 



class Tateti:
    def __init__(self, jugador1, jugador2): #el constructor es: siempre que
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno = self.jugador1
        self.tablero = Tablero()

    def ocupar_una_de_las_casillas(self,fila,columna):
        # pongo la ficha
        self.tablero.poner_la_ficha(fila,columna, self.turno.ficha)
   

        
    def cambiar_turno(self):
        # cambio turno
        if self.turno == self.jugador1:
            self.turno = self.jugador2
        else:
            self.turno = self.jugador1


      #condicicon para ganar
    def hay_ganador(self,ficha):
        #fila
        for fila in self.tablero.obtener_contenedor():
            if fila == [ficha, ficha, ficha]:
                return True
          
        #columna
        for columna in range(3):
            if [self.tablero.obtener_contenedor()[fila][columna] for fila in range(3)] == [ficha, ficha, ficha]:
                return True
            
        #diagonal de izquierda a derecha
        if [self.tablero.obtener_contenedor()[i][i] for i in range(3)] == [ficha, ficha, ficha]:
            return True
        
        #diagonal de derecha a izquierda
        if [self.tablero.obtener_contenedor()[i][2 - i] for i in range(3)] == [ficha, ficha, ficha]:
            return True
        
        return False
