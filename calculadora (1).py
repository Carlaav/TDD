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

    def factorial(self, numero):
        if numero == 0:
            self.value = 1
        else:
            fact = 1
            if numero < 0:
                numero  = -1*numero         
            for i in range(1,numero+1):
                fact = fact * i
            self.value =  fact