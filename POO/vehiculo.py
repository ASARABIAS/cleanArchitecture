from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
 
    def descripcion(self):
        return f"{self.marca} {self.modelo} - Velocidad Mxima: {self.velocidad_maxima} km/h"
 
    @abstractmethod
    def conducir(self):
        pass
 
    @abstractmethod
    def cargar_combustible(self, litros):
        pass