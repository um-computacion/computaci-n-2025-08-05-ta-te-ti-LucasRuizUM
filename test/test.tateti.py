from src.tateti import Tateti
from src.tablero import Tablero
from src.jugador import Jugador
import unittest 

class TestTateti(unittest.TestCase):
    
    def test_init(self):
        jugador1 = Jugador("Jugador1", "X")
        jugador2 = Jugador("Jugador2", "O")
        juego = Tateti(jugador1, jugador2)
        self.assertEqual(juego.turno, jugador1) 
        self.assertIsInstance(juego.tablero, Tablero)
    
    def test_ocupar_casilla(self):
        jugador1 = Jugador("Jugador1", "X")
        jugador2 = Jugador("Jugador2", "O")
        juego = Tateti(jugador1, jugador2)
        juego.ocupar_una_de_las_casillas(1, 1)
        self.assertEqual(juego.tablero.obtener_contenedor()[1][1], "X")
    
    def test_cambiar_turno_x_a_o(self):
        jugador1 = Jugador("Jugador1", "X")
        jugador2 = Jugador("Jugador2", "O")
        juego = Tateti(jugador1, jugador2)
        self.assertEqual(juego.turno, jugador1)
        juego.cambiar_turno()
        self.assertEqual(juego.turno, jugador2)
    
    def test_cambiar_turno_o_a_x(self):
        jugador1 = Jugador("Jugador1", "X")
        jugador2 = Jugador("Jugador2", "O")
        juego = Tateti(jugador1, jugador2)
        juego.turno = jugador2  
        juego.cambiar_turno()
        self.assertEqual(juego.turno, jugador1)
    
    def test_hay_ganador_fila(self):
        jugador1 = Jugador("Jugador1", "X")
        jugador2 = Jugador("Jugador2", "O")
        juego = Tateti(jugador1, jugador2)
        juego.tablero.poner_la_ficha(0, 0, "X")
        juego.tablero.poner_la_ficha(0, 1, "X")
        juego.tablero.poner_la_ficha(0, 2, "X")
        self.assertTrue(juego.hay_ganador("X"))
    
    def test_hay_ganador_columna(self):
        jugador1 = Jugador("Jugador1", "X")
        jugador2 = Jugador("Jugador2", "O")
        juego = Tateti(jugador1, jugador2)
        juego.tablero.poner_la_ficha(0, 0, "X")
        juego.tablero.poner_la_ficha(1, 0, "X")
        juego.tablero.poner_la_ficha(2, 0, "X")
        self.assertTrue(juego.hay_ganador("X"))
    
    def test_hay_ganador_diagonal_principal(self):
        jugador1 = Jugador("Jugador1", "X")
        jugador2 = Jugador("Jugador2", "O")
        juego = Tateti(jugador1, jugador2)
        juego.tablero.poner_la_ficha(0, 0, "X")
        juego.tablero.poner_la_ficha(1, 1, "X")
        juego.tablero.poner_la_ficha(2, 2, "X")
        self.assertTrue(juego.hay_ganador("X"))
    
    def test_hay_ganador_diagonal_secundaria(self):
        jugador1 = Jugador("Jugador1", "X")
        jugador2 = Jugador("Jugador2", "O")
        juego = Tateti(jugador1, jugador2)
        juego.tablero.poner_la_ficha(0, 2, "X")
        juego.tablero.poner_la_ficha(1, 1, "X")
        juego.tablero.poner_la_ficha(2, 0, "X")
        self.assertTrue(juego.hay_ganador("X"))
    
    def test_no_hay_ganador(self):
        jugador1 = Jugador("Jugador1", "X")
        jugador2 = Jugador("Jugador2", "O")
        juego = Tateti(jugador1, jugador2)
        self.assertFalse(juego.hay_ganador("X"))