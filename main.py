import networkx as nx
import numpy as np
from EdgeClass import Link
from NodeClass import Nodo

def definir_status(lista):
    for item in lista:
        item.set_status()
    return

def definir_links_activos(lista):
    for item in lista:
        item.set_value()

Red = nx.Graph()
lista_nodos = {}
lista_links = ''
for i in range(4039):
    status = np.random.choice(1, 0)
    nodo = Nodo(i, status )
    lista_nodos[i] = nodo


for i in lista_nodos.values():
    Red.add_node(i)

data = open('facebook_combined.txt', 'r')
for line in data:
    target_id1 = int(line.split(" ")[0])
    target_id2 = int(line.split(" ")[1])
    Red.add_edge(lista_nodos[target_id1],lista_nodos[target_id2], object=Link(target_id1, target_id2))
data.close()
for iteracion in range(100):
    definir_status(Red.nodes)
    definir_links_activos(Red.edges)
    pass #Aqui van los diversos
print(Red.number_of_nodes())
print(Red.number_of_edges())
