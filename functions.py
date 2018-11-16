import numpy as np

def definir_status(lista):
    p = np.random.uniform()
    for item in lista:
        item.set_status(p)
    return

def definir_links_activos(lista):
    for item in lista:
        item[2]['object'].set_value()


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
