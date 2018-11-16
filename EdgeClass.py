import numpy as np

class Link:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
        self.value = ''

    def set_value(self):
        # distribucion de probabilidad
        self.value = np.random.choice([True,False])
        #return self.value
