from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, puertas):
        super().__init__(marca, modelo, velocidad_maxima)
        self.puertas = puertas

    def conducir(self):
        return f"Conduciendo un auto {self.descripcion()} con {self.puertas} puertas."
    
    def cargar_combustible(self, litros):
        return f"Cargando {litros} litros de combustible en el auto {self.marca} {self.modelo}."