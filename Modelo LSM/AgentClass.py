import numpy as np
import parameters as p
from sklearn import linear_model

class Agente:
    def __init__(self,monitoreo):
        self.umbral = p.umbral_percepcion_agente
        self.sectores = monitoreo
        self.sesgo_normal = np.random.triangular(0,p.sesgo_desviacion_estandar,1) #Triangular o uniforme
        self.sesgo_especialista = np.random.triangular(0,p.sesgo_desviacion_estandar_especialista,1) #triangular u uniforme
        self.especialidades = ''
        self.historico = {}
        while self.sesgo_normal <= self.sesgo_especialista or self.sesgo_normal > 1 or self.sesgo_especialista > 1:
            self.sesgo_normal = np.random.triangular(0,p.sesgo_desviacion_estandar,1) #Triangular o uniforme
            self.sesgo_especialista = np.random.triangular(0,p.sesgo_desviacion_estandar_especialista,1) #triangular u uniforme

    # def set_sesgo_especialista(self):
    #     self.sesgo_especialista = np.random.normal(0,p.sesgo_desviacion_estandar_especialista)
    #
    # def set_sesgo_normal(self):
    #     self.sesgo_normal = np.random.normal(0,p.sesgo_desviacion_estandar)

    def forecast(self):
        cuenta_atras = len(self.historico) - p.memoria_agentes
        data_historico = [self.historico[i] for i in range(cuenta_atras,len(self.historico))]
        data_tiempo = [[i] for i in range(cuenta_atras,len(self.historico))]
        print(data_tiempo)
        regr = linear_model.LinearRegression()
        regr.fit(data_tiempo, data_historico)
        predictions = regr.predict([[len(self.historico)]])
        return predictions
