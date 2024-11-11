class Motor:
    def __init__(self, numero_cilindros, tipo, registro):
        self.numero_cilindros = numero_cilindros
        self.tipo = tipo
        self.registro = registro

    def cambiar_registro(self, registro):
        self.registro = registro

    def asignar_tipo(self, tipo):
        if tipo in ["gasolina", "electrico"]:
            self.tipo = tipo