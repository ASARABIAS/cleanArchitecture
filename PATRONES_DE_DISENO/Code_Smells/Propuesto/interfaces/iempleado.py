from abc import ABC, abstractmethod

class IEmpleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass
