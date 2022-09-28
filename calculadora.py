#calculator.py
from cmath import nan


class Calculator:

    def __init__(self):
        self.value = 0

    def add(self, a, b):
        self.value = a + b

    def restar(self, a, b):
        self.value = a - b

    def multiplicar(self, a, b):
        self.value = a * b

    def dividir(self, a, b):

        if b == 0:
            self.value =  nan
        else:
            self.value = a / b

    def potencia(self,a,b):

        self.value = a ** b