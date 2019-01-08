import random
from parameters import *

class Fenomeno:
    def __init__(self):
        self.intensidad = 0
        self.estado = ''
        self.sector = ''

    def cambiar_estado(self):
        if self.estado == 'inactivo':
            if random.random() < probabilidad_transicion_inactivo_latente:
                self.estado = 'latente'
