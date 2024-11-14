from empleado import Empleado
from informe import Informe

# Uso
if __name__ == "__main__": # para el ejecutor del programa manejar otra clase como main
 empleado = Empleado("Rodrigo Silva", "Ingeniero de Software", 
90000)
 informe = Informe.generar_informe(empleado)
 print(informe)
