class GestorBaseDeDatos: 
    def guardar_en_base_de_datos(self, empleado): 
        print(f"Guardando en la base de datos: {empleado.nombre}, salario: {empleado.salario_base}")