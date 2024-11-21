from modelos.empleado_gerente import EmpleadoGerente
from servicios.impresora_empleado import ImpresoraEmpleado
from servicios.repositorio_empleado import RepositorioEmpleado

# Código ejecutable para probar la clase
if __name__ == "__main__":
    empleado = EmpleadoGerente("Gerente de Ventas", 5000)
    salario_total = empleado.calcular_salario()
    ImpresoraEmpleado.imprimir_detalles_empleado(empleado)
    RepositorioEmpleado.guardar_en_base_de_datos(empleado)
