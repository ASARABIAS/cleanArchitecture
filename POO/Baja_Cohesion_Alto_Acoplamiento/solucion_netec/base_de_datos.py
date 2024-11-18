class BaseDeDatos:
    def guardar(self, empleado):
        print(f"Guardando en la base de datos: {empleado.nombre}, salario: {empleado.salario_base}")