class Nodo:
    def __init__(self,id,Status):
        self.id = id
        self.status = Status
        self.predisposicion = None
        self.memory = {}
        self.opinion = ''

    def __repr__(self):
        return str(self.id)

    @property
    def status(self):
        # distribucion de probabilidad
        return ''
