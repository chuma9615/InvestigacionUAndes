import numpy as np

class Nodo:
    def __init__(self,id,Status):
        self.id = id
        self.stat = Status
        self.predisposicion = None
        self.memory = {}
        self.opinion = ''

    def __repr__(self):
        return str(self.id)

    @property
    def status(self):
        # distribucion de probabilidad
        return np.random.choice([1,0])

    def set_status(self):
        self.stat = np.random.choice([1,0])
