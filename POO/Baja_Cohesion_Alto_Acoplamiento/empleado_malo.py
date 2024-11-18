class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
 
    def calcular_salario(self, horas_extras):
        salario = self.salario_base + (horas_extras * 20)
        return salario
    
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificacin a {self.nombre}: {mensaje}")
 
    def guardar_en_base_de_datos(self):
        print(f"Guardando en la base de datos: {self.nombre}, salario: {self.salario_base}")