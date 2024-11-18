class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
 
    def calcular_salario(self, horas_extras):
        return self.salario_base + (horas_extras * 20)
