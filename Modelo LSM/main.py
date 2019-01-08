import numpy as np
from parameters import *

for iteracion in range(40):
    signal = np.sin(2*np.pi*iteracion/ciclo_senal)
    print(signal)
