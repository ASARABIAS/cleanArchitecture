from modelos.empleado import Empleado

class EmpleadoGerente(Empleado):
    def calcular_salario(self):
        self.bonus = self.salario * 0.20
        return self.salario + self.bonus
