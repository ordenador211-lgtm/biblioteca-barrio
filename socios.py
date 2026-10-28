# socios.py
from datetime import datetime

class Socio:
    def __init__(self, id_socio, nombre):
        self.id_socio = id_socio
        self.nombre = nombre
        self.libros_prestados = [] # Lista de IDs de libros
        self.sancionado_hasta = None # Objeto datetime si está sancionado

    def esta_sancionado(self):
        if self.sancionado_hasta and datetime.now() < self.sancionado_hasta:
            return True
        self.sancionado_hasta = None # Expira la sanción si ya pasó el tiempo
        return False

class Socios:
    def __init__(self):
        self.socios = {} # id_socio -> Objeto Socio

    def dar_de_alta(self, id_socio, nombre):
        if id_socio in self.socios:
            return False, "El socio ya existe."
        self.socios[id_socio] = Socio(id_socio, nombre)
        return True, "Socio dado de alta correctamente."

    def obtener(self, id_socio):
        return self.socios.get(id_socio)