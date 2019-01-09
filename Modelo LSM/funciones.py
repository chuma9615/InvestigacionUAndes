import numpy as np
import parameters as p

def creciente(length=p.ciclo_senal,lower=0,upper=1):
    for i in range(length+1):
        yield (upper-lower)*i/length + lower

def decreciente(length=p.ciclo_senal,lower=0,upper=1):
    for i in range(length+1):
        yield upper - (upper-lower)*i/length

def sinusoidal(length=p.ciclo_senal):
    for iteracion in range(length):
        yield np.sin(2*np.pi*iteracion/length)

def escalon(length=p.ciclo_senal):
    for iteracion in range(length):
        if iteracion < length/2:
            yield 0
        else:
            yield 1
