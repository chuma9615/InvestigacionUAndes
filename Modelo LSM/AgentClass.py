import numpy as np
import parameters as p
from sklearn import linear_model
import pprint
pp = pprint.PrettyPrinter(indent=4)

class Agente:
    """
    Clase que representa a los agentes del modelo

    __init__:
            monitoreo: sectores de fenomenos que el agente a generar estará monitoreando (obligatorio)

            umbral: Umbral numerico por el cual cualquier señal sobre este umbral
                el agente comienza a percibir las señales de los fenomenos

            sesgo_normal: Sesgo con el cual el agente percibe las señales de los fenomenos en el caso de
                que el agente esté percibiendo una señal de la cual no es especialista, se modela mediante
                na distribucion de probabilidad triangular

            sesgo_especialista: Sesgo con el cual el agente percibe las señales de los fenomenos en el caso de
                que el agente esté percibiendo una señal de la cual es especialista, se modela mediante
                na distribucion de probabilidad triangular

            historico: diccionario donde la llave es el numero de iteracion y el valor es
                    un diccionario con la siguiente estructura
                    {'sector': ,'intensidad': ,'sobre_umbral': ,'señal': }

            historico_forecast: diccionario donde se va almacenando el forecast de los agentes en donde la llave
                    es el numero de iteracion predecida y el valor es el valor predecido de la señal

            Notar que en el init se asegura que el sesgo normal siempre sea más grande que el sesgo especialista, cosa de que
                haya una ventaja al percatar fenomenos donde agente es especialista
    """
    def __init__(self,monitoreo):
        self.umbral = p.umbral_percepcion_agente
        self.sectores = monitoreo
        self.sesgo_normal = np.random.triangular(0,p.sesgo_normal,1) #Triangular o uniforme
        self.sesgo_especialista = np.random.triangular(0,p.sesgo_especialista,1) #triangular u uniforme
        self.especialidades = ''
        self.historico = { y:{'sector '+str(x):{z:{} for z in range(p.fenomenos_por_sector) } for x in monitoreo} for y in range(p.numero_iteraciones) }
        self.historico_forecast = {x:0 for x in range(p.numero_iteraciones)} #Arreglar esta parte para tener consistencia
        while self.sesgo_normal <= self.sesgo_especialista or self.sesgo_normal > 1 or self.sesgo_especialista > 1:
            self.sesgo_normal = np.random.triangular(0,p.sesgo_normal,1) #Triangular o uniforme
            self.sesgo_especialista = np.random.triangular(0,p.sesgo_especialista,1) #triangular u uniforme

    # def set_sesgo_especialista(self):
    #     self.sesgo_especialista = np.random.normal(0,p.sesgo_desviacion_estandar_especialista)
    #
    # def set_sesgo_normal(self):
    #     self.sesgo_normal = np.random.normal(0,p.sesgo_desviacion_estandar)

    def forecast(self,iteracion,sector,fenomeno):
        """
        forecast()

            Funcion encargada de realizar el forecast de las señales de fenomenos a observar mediante una regresion lineal de
                datos historicos que el agente recuerda (la memoria del agente puede ser seteada en parameters.py)

            input:
                iteracion: int, Numero de iteracion desde la cual se esta haciendo la predicción

            output:
                predictions: list,  valor de la prediccion de la siguiente iteracion

        """
        """ Si todavia no hay memoria suficiente para hacer la regresion se setea la cuenta atras en cero para que
                esta no se llevea cabo, de lo contrario se ejecuta """
        if iteracion - p.memoria_agentes < 0:
            cuenta_atras = 0
        else:
            cuenta_atras = iteracion - p.memoria_agentes
            """ Se recopilan los datos historicos de percepcion del  """
            # pp.pprint(self.historico)
            data_historico = [self.historico[i]['sector '+str(sector)][fenomeno]['intensidad'] for i in range(cuenta_atras,iteracion)]
            # pp.pprint(data_historico)
            data_tiempo = [[i] for i in range(cuenta_atras,iteracion)]
            regr = linear_model.LinearRegression()
            regr.fit(data_tiempo, data_historico)
            predictions = regr.predict([[len(self.historico)]])
            for predi in predictions:
                self.historico_forecast[iteracion] = predi
                # iteracion += 1
            return predictions
