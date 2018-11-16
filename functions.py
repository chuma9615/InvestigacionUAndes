import numpy as np
import networkx as nx

def definir_status(lista):
    p = np.random.uniform()
    for item in lista:
        item.set_status(p,True)
    p = np.random.uniform()
    for item in lista:
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
    for subgrafo in nx.connected_component_subgraphs(red):
        aux = []
        for edge in subgrafo.edges(data=True):
            if not edge[2]['object'].value:
                aux.append(edge)
        subgrafo.remove_edges_from(aux)

        for nodo in subgrafo:
            status_conexo = []
            for no2 in nx.algorithms.components.node_connected_component(subgrafo,nodo):
                status_conexo.append(no2.stat)
            nodo.memory[iteracion]=status_conexo


            # print('El {} tiene en su  ')



        # for item in subred:

        break
    pass
