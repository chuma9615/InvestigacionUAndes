import random
from parameters import *
import numpy as np
import funciones as func
import parameters as p

class Fenomeno:
    def __init__(self,sector):
        self.intensidad = 0
        self.estado = 'inactivo'
        self.senal = np.random.choice((func.creciente(),func.decreciente(),func.sinusoidal(),func.escalon(),func.randomwalk()))
        self.sector = sector
        self.historico = {}

        # {'creciente':func.creciente,'decreciente':func.decreciente,'sin':func.sinusoidal,'escalon':func.escalon}
        # self.senal = ''
    @property
    def ruido(self):
        return np.random.triangular(0,p.ruido_fenomeno,1)

    def cambiar_estado(self):
        if self.estado == 'inactivo':
            if random.random() < probabilidad_transicion_inactivo_latente:
                self.estado = 'latente'


    def calcular_intensidad(self,iteracion):
        try:
            senal = next(self.senal)
            ruido = self.ruido
            self.intensidad = senal + ruido
            self.historico[iteracion] = {'señal':senal,'ruido':ruido,'intensidad':self.intensidad}
        except StopIteration:
            pass
