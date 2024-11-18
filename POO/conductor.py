class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculo = None
 
    def asignar_vehiculo(self, vehiculo):
        self.vehiculo = vehiculo
        print(f"{self.nombre} ahora est conduciendo un {vehiculo.marca} {vehiculo.modelo}.")
 
    def conducir(self):
        if self.vehiculo:
            print(self.vehiculo.conducir())
        else:
            print(f"{self.nombre} no tiene un vehculo asignado.")
 
    def cargar_combustible(self, litros):
        if self.vehiculo:
            print(self.vehiculo.cargar_combustible(litros))
        else:
            print(f"{self.nombre} no tiene un vehculo asignado para cargar combustible.")