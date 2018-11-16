import networkx as nx
import numpy as np
from EdgeClass import Link
from NodeClass import Nodo
import matplotlib
from functions import *



Red = nx.Graph()
lista_nodos = {}
lista_links = ''
for i in range(4039):
     # """En este ciclo se instancian los nodos
     #        con una id particular y se guardan en el diccionario"""
    nodo = Nodo(i)
    nodo.calculate_predisposition
    lista_nodos[i] = nodo


for i in lista_nodos.values():
    # """ En este ciclo se agregan los nodos al objeto grafo """
    Red.add_node(i)


data = open('facebook_combined.txt', 'r')
for line in data:
    """ En este ciclo se agregan los arcos """
    aux = line.split(" ")
    target_id1 = int(aux[0])
    target_id2 = int(aux[1])
    Red.add_edge(lista_nodos[target_id1],lista_nodos[target_id2], object=Link(target_id1, target_id2))
data.close()

lista_arcos = Red.edges()

predisposicion_0 = calcular_ratio_predisposicion(Red.nodes)

iteraciones = 1

for iteracion in range(iteraciones): #
    definir_status(Red.nodes)
    definir_links_activos(Red)
    ratio_global = calcular_ratio_activos(Red.nodes)
    #print(ratio_global)
    propagar_informacion(Red,iteracion)
     #Aqui van los diversos
# print(Red.get_edge_data(lista_nodos[0],lista_nodos[1])['object'].set_value)
nodos = list(Red.nodes())
print(nodos[0].memory)
print(Red.number_of_nodes())
print(Red.number_of_edges())
