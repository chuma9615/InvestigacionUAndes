import numpy as np
import networkx as nx
import setup
from copy import deepcopy

def definir_status(lista):
    p = setup.distribucion_definir_status(*setup.parametros_definir_status)
    for item in lista:
        if item.stat:
            item.set_status(p,True)
        if not item.stat:
            item.set_status(p,False)
    return

def definir_links_activos(red):
    lista = red.edges(data=True)
    remove = []
    for item in lista:
        item[2]['object'].set_value()
    return



def calcular_ratio_predisposicion(nodos):
    ratio = {'Positivo':0 , 'Negativo': 0, 'Neutro': 0}
    for item in nodos:
        if item.predisposicion == -1:
            ratio['Negativo']+=1
        elif item.predisposicion == 1:
            ratio['Positivo']+=1
        elif item.predisposicion == 0:
            ratio['Neutro']+=1

    return ratio

def calcular_ratio_activos(nodos):
    activos = 0
    for nodo in nodos:
        if nodo.stat:
            activos+=1
    ratio = activos/len(nodos)
    return ratio

def propagar_informacion(red,iteracion):
    red2 = deepcopy(red)
    for subgrafo in nx.connected_component_subgraphs(red):
        aux = []
        for edge in subgrafo.edges(data=True):
            if not edge[2]['object'].value:
                aux.append(edge)
        # print(aux)
        subgrafo.remove_edges_from(aux)
        red2.remove_edges_from(aux)
        for nodo in subgrafo.nodes:
            # print(nodo)
            status_conexo = [no2.stat for no2 in nx.algorithms.components.node_connected_component(subgrafo,nodo)]
            nodo.memory[iteracion]=status_conexo


            # print('El {} tiene en su  ')



        # for item in subred:


    return nx.average_clustering(red2)
