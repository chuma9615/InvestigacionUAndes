import numpy as np

class Nodo:
    def __init__(self,id,Status = 0):
        self.id = id
        self.stat = np.random.choice([True,False])
        self.predisposicion = None
        self.memory = {}
        self.opinion = ''

    def __repr__(self):
        return str(self.id)


    @property
    def calculate_predisposition(self):
        #En cada ronda se calcula la predisposicion del ciudadano usando distribucion Uniforme 0,1
        numero = np.random.uniform()
        if numero < 0.3:
            self.predisposicion = -1
        elif numero > 0.7:
            self.predisposicion = 1
        else:
            self.predisposicion = 0


    def set_status(self,probabilidad=1):
        numero = np.random.uniform()
        if numero < probabilidad:
            if self.stat:
                self.stat = False
            elif not self.stat:
                self.stat = True
