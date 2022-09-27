

def factorial(numero):

    if numero == 0:
        return 1


    fact = 1

    if numero < 0:
        numero  = -1*numero 
    
    for i in range(1,numero+1):
        fact = fact * i
    
    return fact
