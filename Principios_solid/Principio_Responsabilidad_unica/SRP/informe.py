from empleado import Empleado

class Informe:

    @staticmethod
    def generar_informe(empleado: Empleado): #Se podria mejorar generando una clase para informe
        return f"Informe del Empleado: {empleado.obtener_detalles()}"
