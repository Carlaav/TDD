

import unittest

from calculadora import Calculator


class TestMyCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)
        # Creamos un nuevo test para comprobar una suma

    def test_add_method(self):
        # Ejecutamos el método
        self.calc.add(1, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(4, self.calc.value)

    def test_restar_method(self):
        # Ejecutamos el método
        self.calc.restar(1, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(-2, self.calc.value)

    def test_multiplicar_method(self):
        # Ejecutamos el método
        self.calc.multiplicar(1, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(3, self.calc.value)

    def test_dividir_method(self):
        # Ejecutamos el método
        self.calc.dividir(6, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(2, self.calc.value)

    def test_potencia_method(self):
        # Ejecutamos el método
        self.calc.potencia(1, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(1, self.calc.value)

    def test_factorial_method(self):
        # Ejecutamos el método
        self.calc.factorial(50)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(30414093201713378043612608166064768844377641568960512000000000000, self.calc.value)
