from empleado import Empleado
from salario import CalculadoraSalario
from notificacion import Notificador
from base_de_datos import BaseDeDatos

def main():
    empleado = Empleado("Rodrigo", 1000)
    calculadora = CalculadoraSalario()
    notificador = Notificador()
    base_de_datos = BaseDeDatos()
    horas_extras = 10
    salario = calculadora.calcular_salario(empleado, horas_extras)
    print(f"Salario calculado: {salario}")
    notificador.enviar_notificacion(empleado, f"Su salario ha sido calculado: ${salario}")
    base_de_datos.guardar(empleado)
    
if __name__ == "__main__":
 main()
