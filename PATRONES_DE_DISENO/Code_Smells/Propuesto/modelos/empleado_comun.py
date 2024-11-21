from modelos.empleado import Empleado

class EmpleadoComun(Empleado):
    def calcular_salario(self):
        self.bonus = self.salario * 0.10
        return self.salario + self.bonus
