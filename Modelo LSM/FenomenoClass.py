import random
from parameters import *
import numpy as np
import funciones as func

class Fenomeno:
    def __init__(self):
        self.intensidad = 0
        self.estado = ''
        self.sector = ''
        self.senal = np.random.choice((func.creciente,func.decreciente,func.sinusoidal,func.escalon))
        self.ruido =  np.random.triangular(0,p.ruido_fenomeno,1)


        # {'creciente':func.creciente,'decreciente':func.decreciente,'sin':func.sinusoidal,'escalon':func.escalon}
        # self.senal = ''

    def cambiar_estado(self):
        if self.estado == 'inactivo':
            if random.random() < probabilidad_transicion_inactivo_latente:
                self.estado = 'latente'
        elif self.estado == 'latente':
            if self.intensidad > self.umbral:
                self.estado == 'activo'
            elif self.intensidad < self.umbral:
                pass
    def calcular_intensidad(self):
        self.intensidad = next(self.senal)

a = Fenomeno()
for i in range(49):
    a.calcular_intensidad()

print(a.intensidad)
