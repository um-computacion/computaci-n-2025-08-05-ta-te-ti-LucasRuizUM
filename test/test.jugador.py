import unittest
from src.jugador import Jugador
from src.excepciones import FichaInvalidaError, NombreVacioError


class TestJugador(unittest.TestCase):
    
    def setUp(self):
        self.jugador_x = Jugador("Ana", "X")
        self.jugador_o = Jugador("Carlos", "O")
    
    def test_creacion_jugador_valido(self):
        self.assertEqual(self.jugador_x.nombre, "Ana")
        self.assertEqual(self.jugador_x.ficha, "X")
        self.assertEqual(self.jugador_o.nombre, "Carlos")
        self.assertEqual(self.jugador_o.ficha, "O")
    
    def test_nombres_diferentes(self):
        jugador1 = Jugador("María", "X")
        jugador2 = Jugador("Pedro", "O")
        self.assertEqual(jugador1.nombre, "María")
        self.assertEqual(jugador2.nombre, "Pedro")
        self.assertNotEqual(jugador1.nombre, jugador2.nombre)
    
    def test_fichas_diferentes(self):
        jugador1 = Jugador("Luis", "X")
        jugador2 = Jugador("Luis", "O")
        self.assertEqual(jugador1.ficha, "X")
        self.assertEqual(jugador2.ficha, "O")
        self.assertNotEqual(jugador1.ficha, jugador2.ficha)
    
    def test_str_representation(self):
        test_cases = [
            (Jugador("Sofia", "X"), "Jugador: Sofia ficha: X"),
            (Jugador("Diego", "O"), "Jugador: Diego ficha: O"),
            (Jugador("Alejandro", "X"), "Jugador: Alejandro ficha: X"),
            (Jugador("A", "O"), "Jugador: A ficha: O")
        ]
        for jugador, expected in test_cases:
            with self.subTest(jugador=jugador.nombre):
                self.assertEqual(str(jugador), expected)
    
    def test_modificar_atributos(self):
        jugador = Jugador("Juan", "X")
        jugador.nombre = "Nuevo Juan"
        jugador.ficha = "O"
        self.assertEqual(jugador.nombre, "Nuevo Juan")
        self.assertEqual(jugador.ficha, "O")
    
    def test_igualdad_objetos(self):
        jugador1 = Jugador("Roberto", "X")
        jugador2 = Jugador("Roberto", "X")
        jugador3 = jugador1
        self.assertNotEqual(jugador1, jugador2)
        self.assertIsNot(jugador1, jugador2)
        self.assertIs(jugador1, jugador3)
    
    def test_ficha_invalida(self):
        with self.assertRaises(FichaInvalidaError):
            Jugador("Invalido", "Z")
    
    def test_nombre_vacio(self):
        with self.assertRaises(NombreVacioError):
            Jugador("", "X")


if __name__ == '__main__':
    unittest.main()