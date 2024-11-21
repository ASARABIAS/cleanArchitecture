from modelos.empleado import Empleado

class EmpleadoDirector(Empleado):
    def calcular_salario(self):
        self.bonus = self.salario * 0.30
        return self.salario + self.bonus
