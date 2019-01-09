import numpy as np
from parameters import *
from AgentClass import *
from SectorClass import *
from FenomenoClass import *
import parameters as p
import pprint


pp = pprint.PrettyPrinter(indent=4)

""" instanciar sectores del modelo"""
 # ['money_market','renta_fija','renta_variable','dolar','mercado_emergente','capital_riesgo']:
sectores = {}
for i in range(cantidad_sectores):
    sectores[i] = [Fenomeno(i) for j in range(p.fenomenos_por_sector)]

""" instanciar agentes del modelo """
agentes = []
for i in range(numero_agentes):
    agent = Agente(np.random.choice(list(sectores.keys()),p.memoria_agentes))
    agentes.append(agent)

""" se corren las iteraciones """
for iteracion in range(numero_iteraciones):
    for sector,fenomenos in sectores.items():
        for fenomeno in fenomenos:
            if fenomeno.estado == 'inactivo':
                fenomeno.cambiar_estado()
            elif fenomeno.estado != 'inactivo':
                fenomeno.calcular_intensidad(iteracion)
                # print(fenomeno.historico)
    for agente in agentes:
        for sector in agente.sectores:
            for sector2 in sectores[sector]:
                if sector2.intensidad > agente.umbral:
                    agente.historico[iteracion] = {'intenisdad':sector2.intensidad,'sobre_umbral':True}

                else:
                    agente.historico[iteracion] = {'intenisdad':sector2.intensidad,'sobre_umbral':False}



for key,value in sectores.items():
    print(key)
    for fenomeno in value:
        pp.pprint(fenomeno.historico)

for agente in agentes:
    pp.pprint(agente.historico)
