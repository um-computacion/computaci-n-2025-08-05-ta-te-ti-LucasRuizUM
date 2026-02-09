from unittest.mock import patch
import unittest
from src import cli

class TestCLI(unittest.TestCase):
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_juego_con_ganador(self, mock_print, mock_input):
        """Test game with a winner scenario"""
        # Simulate player inputs for a winning game
        mock_input.side_effect = [
            "Jugador1", "Jugador2",  # Player names
            "0", "0",  # X at (0,0)
            "1", "0",  # O at (1,0)
            "1", "1",  # X at (1,1)
            "2", "0",  # O at (2,0)
            "2", "2"   # X at (2,2) - wins diagonally
        ]
        cli.main()
        mock_print.assert_any_call("El ganador es Jugador1")
    
    @patch('builtins.input')  
    @patch('builtins.print')
    def test_juego_empate(self, mock_print, mock_input):
        """Test game with a tie scenario"""
        # Simulate inputs for a tied game
        mock_input.side_effect = [
            "Jugador1", "Jugador2",
            "0", "0", "0", "1", "0", "2",
            "1", "1", "1", "0", "1", "2",
            "2", "1", "2", "0", "2", "2"
        ]
        cli.main()
        mock_print.assert_any_call("El juego ha terminado en empate")
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_casilla_fuera_de_rango(self, mock_print, mock_input):
        """Test out-of-range position handling"""
        mock_input.side_effect = [
            "Jugador1", "Jugador2",
            "5", "0",  # Invalid position
            KeyboardInterrupt()  # Exit the game
        ]
        with self.assertRaises(KeyboardInterrupt):
            cli.main()
        mock_print.assert_any_call("Esta casilla está fuera de rango. Elige una entre 0 y 2")
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_posicion_ocupada(self, mock_print, mock_input):
        """Test occupied position handling"""
        mock_input.side_effect = [
            "Jugador1", "Jugador2",
            "0", "0",  # First move
            "0", "0",  # Try to play same position
            KeyboardInterrupt()  # Exit the game
        ]
        with self.assertRaises(KeyboardInterrupt):
            cli.main()
        mock_print.assert_any_call("Esta casilla ya está ocupada. Elige otra")

if __name__ == '__main__':
    unittest.main()