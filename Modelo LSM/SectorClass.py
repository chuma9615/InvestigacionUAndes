import numpy as np
import funciones as func

class Sector:
    def __init__(self):
        self.nombre = ''
        self.especialistas = {}
        self.fenomenos = {}
        self.ruido = ''
        self.senal = {'creciente':func.creciente,'decreciente':func.decreciente,'sin':func.sinusoidal,'escalon':func.escalon}
