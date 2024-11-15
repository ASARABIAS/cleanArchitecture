from abc import ABC, abstractmethod

class Almacenamiento(ABC):
    @abstractmethod
    def guardar_orden(self, orden):
        pass