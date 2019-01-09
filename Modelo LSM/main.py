import numpy as np
from parameters import *
from AgentClass import *
from SectorClass import *
from FenomenoClass import *


""" instanciar agentes del modelo """
agentes = []
for i in range(numero_agentes):
    agentes.append(Agente())

for iteracion in range(40):
    signal = np.sin(2*np.pi*iteracion/ciclo_senal)

    ruido = np.random.normal()
print([(i.sesgo_normal,i.sesgo_especialista) for i in agentes ])
