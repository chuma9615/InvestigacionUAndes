import random
from parameters import *
import numpy as np
import funciones as func
import parameters as p

class Fenomeno:
    """
    Clase dedicada a modelar los fenomenos de la simulacion, cada fenomeno tine un sector determinado

    """
    def __init__(self,sector,numero_fenomeno):
        """
        Input:
            sector: sector al cual pertenece el fenomeno especifico (obligatorio)
            intensidad: la intensidad del fenomeno comienza en cero
            senal: se escoje al azar un tipo de señal que será la representacion de
                    la informacion que arroja el fenomeno al medio
            historico: diccionario donde la llave es el numero de iteracion y el valor es
                    un diccionario con la siguiente estructura
                     {'señal': ,'ruido': ,'intensidad': }

        """
        self.numero_fenomeno = numero_fenomeno
        self.intensidad = 0
        self.estado = 'inactivo'
        self.senal = np.random.choice((func.creciente(),func.decreciente(),func.sinusoidal(),func.escalon(),func.randomwalk()))
        self.sector = sector
        self.historico = {}
        # {'creciente':func.creciente,'decreciente':func.decreciente,'sin':func.sinusoidal,'escalon':func.escalon}
        # self.senal = ''


    @property
    def ruido(self):
        """
            Metodo que se encarga de generar el ruido de la señal del fenomeno

            input:
                self

            output:
                retorna un float compuesto por 2 valores, el ruido estandar de los fenomenos
                seteados en parameters.py y una variable aleatoria normal mu=0 sigma=0.05
        """
        return p.ruido_fenomeno + np.random.normal(0,0.05) # promedio en cero

    def cambiar_estado(self):

        """
        cambiar_estado:
            metodo que se encarga de cambiar el estado de un fenomeno de "inactivo" a "latente"
        """
        if self.estado == 'inactivo':
            if random.random() < probabilidad_transicion_inactivo_latente:
                self.estado = 'latente'


    def calcular_intensidad(self,iteracion):
        """
            Metodo que calcula la intensidad de la señal a proyectar en el fenomeno particular por iteracion

            input:
                iteracion: numero de iteracion en la que se encuentra la simulacion

            funcionamiento:
                En un principio, se computa el siguiente valor de la señal, el valor del ruido,
                se guarda la intensidad en la clase y se actualiza el historico con los valores
                de la señal, ruido e intensidad.

                de no existir el valor de la señal (debido a que la señal ya cumplió su ciclo y termino
                de emitir informacion) se levanta un error de StopIteration el que es capturado por el
                except y se procede a volver a dejar al fenomeno inactivo, luego se setea un nuevo tipo de
                señal al azar entre las existentes y finalemnte se anota todo en historico

        """
        try:
            senal = next(self.senal)
            ruido = self.ruido
            self.intensidad = senal + ruido
            self.historico[iteracion] = {'señal':senal,'ruido':ruido,'intensidad':self.intensidad}
        except StopIteration:
            self.intensidad = self.ruido
            self.estado = 'inactivo'
            self.senal = np.random.choice((func.creciente(),func.decreciente(),func.sinusoidal(),func.escalon(),func.randomwalk()))
            #Cambiar generacion señal
            self.historico[iteracion] = {'intensidad':self.intensidad,'señal':0}
