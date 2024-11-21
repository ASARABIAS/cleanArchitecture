from interfaces.iempleado import IEmpleado

class Empleado(IEmpleado):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        self.bonus = 0

    def calcular_salario(self):
        raise NotImplementedError("Debe implementar el método calcular_salario en la subclase")
