import numpy as np
from parameters import *
from AgentClass import *
from SectorClass import *
from FenomenoClass import *
import parameters as p
import pprint
import matplotlib.pyplot as plt



pp = pprint.PrettyPrinter(indent=4)

""" instanciar sectores del modelo"""
 # ['money_market','renta_fija','renta_variable','dolar','mercado_emergente','capital_riesgo']:
sectores = {}
for i in range(cantidad_sectores):
    sectores[i] = [Fenomeno(i) for j in range(p.fenomenos_por_sector)]

""" instanciar agentes del modelo """
agentes = []
for i in range(numero_agentes):
    agent = Agente(np.random.choice(list(sectores.keys()),p.sectores_por_agentes))
    agentes.append(agent)

""" se corren las iteraciones """
for iteracion in range(numero_iteraciones):
    for sector,fenomenos in sectores.items():
        """ Si el fenomeno esta inactivo se activo lanzando una probabilidad y se anota en el historico la informacion"""
        for fenomeno in fenomenos:
            if fenomeno.estado == 'inactivo':
                fenomeno.historico[iteracion] = {'intensidad':fenomeno.intensidad,'señal':0}
                fenomeno.cambiar_estado()
            elif fenomeno.estado != 'inactivo':
                fenomeno.calcular_intensidad(iteracion)
    for agente in agentes:
        """ Los agentes revisan sus sectores y realizan predicciones de ser pertinentes"""
        for sector in agente.sectores:
            for sector2 in sectores[sector]:
                if sector2.intensidad > agente.umbral:
                    agente.historico[iteracion] = {'sector':sector2.sector,'intensidad':sector2.intensidad,'sobre_umbral':True,'señal':sector2.senal}

                if sector2.intensidad < agente.umbral:
                    agente.historico[iteracion] = {'sector':sector2.sector,'intensidad':sector2.intensidad,'sobre_umbral':False,'señal':sector2.senal}

                if p.forecasting and iteracion > p.memoria_agentes:
                    agente.forecast()



"""  Sector de analisis de datos"""
for key,value in sectores.items():
    for fenomeno in value:
        pp.pprint(fenomeno.historico)

for agente in agentes:
    pp.pprint(agente.historico)
    pp.pprint(agente.historico_forecast)

print(sectores[agentes[0].sectores[0]][0].historico)
item = [ x['señal'] for x in list(sectores[agentes[0].sectores[0]][0].historico.values()) ]
item2= [x for x in list(agentes[0].historico_forecast.values())]
print(item,len(item))
print(item2,len(item2))
plt.plot(item)
plt.plot(item2)
plt.show()
