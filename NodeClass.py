import numpy as np
import setup

class Nodo:
    def __init__(self,id,Status = 0):
        self.id = id
        self.stat = np.random.choice([True,False],p=setup.probabilidad_NodeClass_stat)
        self.predisposicion = None
        self.memory = {}
        self.opinion = ''

    def __repr__(self):
        return 'nodo ' + str(self.id)


    @property
    def calculate_predisposition(self):
        #En cada ronda se calcula la predisposicion del ciudadano usando distribucion Uniforme 0,1
        numero = setup.distribucion_calculate_predisposition(*setup.parametros_calculate_predisposition)
        if numero < setup.probabilidad_calculate_predisposition:
            self.predisposicion = -1
        elif numero > 1 - setup.probabilidad_calculate_predisposition:
            self.predisposicion = 1
        else:
            self.predisposicion = 0


    def set_status(self,probabilidad=1,on=True):
        numero = setup.distribucion_set_status(*setup.parametros_set_status)
        if on and self.stat:
            if numero < probabilidad:
                self.stat = False
        if not on and not self.stat:
            if numero < probabilidad:
                self.stat = True
