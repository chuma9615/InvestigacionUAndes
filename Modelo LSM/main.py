import numpy as np
from parameters import *
from AgentClass import *
from SectorClass import *
from FenomenoClass import *
import parameters as p
import pprint
import matplotlib.pyplot as plt

""" Este archivo es el archivo principal que debe ser ejecutado para que se corran las simulaciones,
        engloba todos los otros archivos en un solo código """

pp = pprint.PrettyPrinter(indent=4)

""" crear los diversos sectores donde los agentes irán monitoreando las actividades"""
 # ['money_market','renta_fija','renta_variable','dolar','mercado_emergente','capital_riesgo']:
sectores = {}
for i in range(cantidad_sectores):
    sectores[i] = [Fenomeno(i,j) for j in range(p.fenomenos_por_sector)]

""" crear los agentesde la simulacion, los parametros de estos se setean en parameters.py """
agentes = []
for i in range(numero_agentes):
    monitoreo = np.random.choice(list(sectores.keys()),p.sectores_por_agentes , replace=False)
    print(monitoreo)
    agent = Agente(monitoreo)
    agentes.append(agent)

""" se corren las iteracionen del modelo segun lo seteado en parameters.py"""
for iteracion in range(numero_iteraciones):
    for sector,fenomenos in sectores.items():
        """ Si el fenomeno esta inactivo se activo lanzando una probabilidad y se anota en el historico la informacion"""
        for fenomeno in fenomenos:
            if fenomeno.estado == 'inactivo':
                fenomeno.historico[iteracion] = {'intensidad':fenomeno.intensidad,'señal':0, 'ruido': 0}
                fenomeno.cambiar_estado()
            elif fenomeno.estado != 'inactivo':
                fenomeno.calcular_intensidad(iteracion)
    for agente in agentes:
        """ Los agentes revisan sus sectores y realizan predicciones de ser pertinentes"""
        for sector in agente.sectores:
            for fenomeno in sectores[sector]:
                if p.forecasting and iteracion > p.memoria_agentes:
                    agente.forecast(iteracion,'sector ' + str(sector),fenomeno.numero_fenomeno)

                if fenomeno.intensidad > agente.umbral:
                    agente.historico[iteracion]['sector '+ str(fenomeno.sector)][fenomeno.numero_fenomeno] = {'intensidad':fenomeno.intensidad,'sobre_umbral':True,'señal':fenomeno.senal}

                if fenomeno.intensidad < agente.umbral:
                    agente.historico[iteracion]['sector '+ str(fenomeno.sector)][fenomeno.numero_fenomeno] = {'intensidad':fenomeno.intensidad,'sobre_umbral':False,'señal':fenomeno.senal}

        # pp.pprint(agente.historico)
        # print()
        # print(agente)
        # print()




"""  Sector de analisis de datos"""
for key,value in sectores.items():
    for fenomeno in value:
        pass
        # pp.pprint(fenomeno.historico)

for agente in agentes:
    pp.pprint(agente.historico)
    # pp.pprint(agente.historico_forecast)

# item = [ x['señal'] for x in list(sectores[agentes[0].sectores[0]][0].historico.values()) ]
agente = agentes[0]
sector = 'sector ' + str(agentes[0].sectores[0])
fenomeno = 0
pp.pprint(agente.historico_forecast)
item2= [x[sector][0] for x in list(agente.historico_forecast.values()) ] #Revisar la indexacion de la informacion
# print(sectores[agentes[0].sectores[0]][0].historico , 'dict historico')
item3 = [ x['intensidad'] for x in list(sectores[agentes[0].sectores[0]][0].historico.values()) ]
print(item3,'historico')
print(item2,'forecast')
# print(item,len(item))3
plt.plot(item3)
plt.plot(item2)
plt.legend()
# plt.plot(item3)
plt.show()
