from src.excepciones import Exceptions, CasillaFueradeRango, PosOcupadaExceptions
import unittest


class TestExcepciones(unittest.TestCase):

    def test_pos_ocupada_exception(self):
        with self.assertRaises(PosOcupadaExceptions):
            raise PosOcupadaExceptions("Posición ocupada")
        self.assertTrue(issubclass(PosOcupadaExceptions, Exception))
    
    def test_casilla_fuera_rango_exception(self):
        with self.assertRaises(CasillaFueradeRango):
            raise CasillaFueradeRango("Casilla fuera de rango")
        self.assertTrue(issubclass(CasillaFueradeRango, Exceptions))
    
    def test_exceptions_base(self):
        with self.assertRaises(Exceptions):
            raise Exceptions("Error base")
        self.assertTrue(issubclass(Exceptions, Exception))


if __name__ == '__main__':
    unittest.main()