import numpy as np
import parameters as p

class Agente:
    def __init__(self):
        self.monitoreando = None
        self.sesgo_normal = np.normal(0,p.sesgo_desviacion_estandar)
        self.sesgo_especialista = np.normal(0,p.sesgo_desviacion_estandar_especialista)

    def set_sesgo_especialista(self):
        self.sesgo_especialista = np.normal(0,p.sesgo_desviacion_estandar_especialista)

    def set_sesgo_normal(self):
        self.sesgo_normal = np.normal(0,p.sesgo_desviacion_estandar)
