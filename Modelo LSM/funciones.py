import numpy as np
import parameters as p

def creciente(length=p.ciclo_senal,lower=0,upper=1):
    """ Funcion encargada de crear una señal creciente,
        la cual a cada llamado va devolviendo un valor determinado

        input:
                Length: numero de iteraciones a simulart por señal
                lower: cota inferior de la señal
                upper: cota superior de la señal

        output:
                yield, valor actual del ciclo solicitado.
                    (Para mas info sobre como funciona un yield, mirar documentacion de python) """
    for i in range(length+1):
        yield (upper-lower)*i/length + lower


def decreciente(length=p.ciclo_senal,lower=0,upper=1):
    """ Funcion encargada de crear una señal decreciente,
            la cual a cada llamado va devolviendo un valor determinado

            input:
                    Length: numero de iteraciones a simulart por señal
                    lower: cota inferior de la señal
                    upper: cota superior de la señal

            output:
                    yield, valor actual del ciclo solicitado.
                    (Para mas info sobre como funciona un yield, mirar documentacion de python)"""
    for i in range(length+1):
        yield upper - (upper-lower)*i/length

def sinusoidal(length=p.ciclo_senal):
    """ Funcion encargada de crear una señal sinusoidal,
            la cual a cada llamado va devolviendo un valor determinado

            input:
                    Length: numero de iteraciones a simulart por señal
                    lower: cota inferior de la señal
                    upper: cota superior de la señal

            output:
                    yield, valor actual del ciclo solicitado.
                        (Para mas info sobre como funciona un yield, mirar documentacion de python)
                        """
    for iteracion in range(length):
        yield np.sin(2*np.pi*iteracion/length)

def escalon(length=p.ciclo_senal):
    """ Funcion encargada de crear una señal de escalon,
            la cual a cada llamado va devolviendo un valor determinado segun la funcion escalon

            input:
                    Length: numero de iteraciones a simulart por señal
            output:
                     0 cuando va en la mitad inferior del rango
                     1 cuando va en la mitad inferior del rango
                        """
    for iteracion in range(length):
        if iteracion < length/2:
            yield 0
        else:
            yield 1

def randomwalk(length=p.ciclo_senal):
    """
    Funcion encargada de simular un random walk, el mu y sigma de
        la distribucion normal son seteados desde parameters.py

        Si el valor del random walk a retornar se pasa del rango [0,1] se aproxima a la cota más cercana

    input:
        Length: numero de iteraciones a simulart por señal

    output:
        devuelve el valor actual de el rw

    """
    rw = 0
    for iteracion in range(length):
        yield rw
        rw = rw + np.random.normal(p.mu_rw,p.sigma_rw)
        if rw >1:
            rw = 1
        if rw < 0:
            rw = 0
