from empleado import Empleado
from calculadora_salario import CalculadoraSalario
from notificador import Notificador
from gestor_db import GestorBaseDeDatos

empleado = Empleado("Juan", 1000) 
calculadora = CalculadoraSalario() 
notificador = Notificador() 
estor_bd = GestorBaseDeDatos() 
salario_total = calculadora.calcular_salario(empleado, 10) 
notificador.enviar_notificacion(empleado, "Tu salario ha sido calculado.")