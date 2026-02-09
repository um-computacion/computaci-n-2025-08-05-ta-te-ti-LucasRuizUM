from src.tablero import Tablero
from src.excepciones import PosicionOcupadaError, CasillaFueraDeRangoError
import unittest


class TestTablero(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()
        
        self.tablero_ejemplo = Tablero()
        self.tablero_ejemplo.poner_ficha(0, 0, "X")
        self.tablero_ejemplo.poner_ficha(1, 1, "O")
    
    def test_inicializacion_tablero(self):
        contenido = self.tablero.obtener_contenido()
        
       
        self.assertEqual(len(contenido), 3, "El tablero debe tener 3 filas")
        for fila in contenido:
            self.assertEqual(len(fila), 3, "Cada fila debe tener 3 columnas")
            self.assertEqual(fila, ["", "", ""], "Todas las celdas deben estar vacías al inicio")
    
    def test_colocar_ficha_valida(self):
        casos_prueba = [
            (0, 0, "X"),  
            (1, 1, "O"),
            (2, 2, "X"),  
            (0, 2, "O"),  
            (2, 0, "X")   
        ]
        
        for fila, col, ficha in casos_prueba:
            with self.subTest(fila=fila, col=col, ficha=ficha):
                self.tablero.poner_ficha(fila, col, ficha)
                self.assertEqual(
                    self.tablero.obtener_contenido()[fila][col],
                    ficha,
                    f"La celda ({fila},{col}) debería contener {ficha}"
                )
    
    def test_colocar_ficha_fuera_rango(self):
        posiciones_invalidas = [
            (-1, 0), (3, 0),   
            (0, -1), (0, 3),    
            (-1, -1), (3, 3),    
            (1.5, 2), (0, "a")  
        ]
        
        for fila, col in posiciones_invalidas:
            with self.subTest(fila=fila, col=col):
                with self.assertRaises(CasillaFueraDeRangoError):
                    self.tablero.poner_ficha(fila, col, "X")
    
    def test_colocar_ficha_posicion_ocupada(self):
        with self.assertRaises(PosicionOcupadaError):
            self.tablero_ejemplo.poner_ficha(0, 0, "O")
        
        self.assertEqual(
            self.tablero_ejemplo.obtener_contenido()[0][0],
            "X",
            "La ficha original debe permanecer"
        )
    
    def test_tablero_lleno(self):
        self.assertFalse(
            self.tablero.tablero_lleno(),
            
        )
        
       
        for fila in range(3):
            for col in range(3):
                self.tablero.poner_ficha(fila, col, "X")
        
        self.assertTrue(
            self.tablero.tablero_lleno(),
            
        )
        
     
        self.tablero.obtener_contenido()[1][1] = ""
        self.assertFalse(
            self.tablero.tablero_lleno(),
           
        )
    
    def test_limpiar_tablero(self):
   
        for fila in range(3):
            for col in range(3):
                self.tablero.poner_ficha(fila, col, "X")
        
        self.tablero.limpiar_tablero()
        
        
        for fila in range(3):
            for col in range(3):
                self.assertEqual(
                    self.tablero.obtener_contenido()[fila][col],
                    "",
                    f"La celda ({fila},{col}) debe estar vacía"
                )
    
    def test_representacion_string(self):
        tablero_str = str(self.tablero)
        self.assertIn("0,0:  | 0,1:  | 0,2: ", tablero_str)
        
        
        tablero_str = str(self.tablero_ejemplo)
        self.assertIn("0,0: X", tablero_str)
        self.assertIn("1,1: O", tablero_str)


if __name__ == '__main__':
    unittest.main(verbosity=2)