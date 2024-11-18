from vehiculo import Vehiculo
class Camion(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, capacidad_carga):
        super().__init__(marca, modelo, velocidad_maxima)
        self.capacidad_carga = capacidad_carga

    def conducir(self):
        return f"Conduciendo un camin {self.descripcion()} con capacidad de {self.capacidad_carga} toneladas."
 
    def cargar_combustible(self, litros):
        return f"Cargando {litros} litros de combustible en el camin {self.marca} {self.modelo}."
