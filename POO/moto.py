from vehiculo import Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, cilindrada):
        super().__init__(marca, modelo, velocidad_maxima)
        self.cilindrada = cilindrada
 
    def conducir(self):
        return f"Conduciendo una moto {self.descripcion()} de {self.cilindrada}cc."
 
    def cargar_combustible(self, litros):
        return f"Cargando {litros} litros de combustible en la moto {self.marca} {self.modelo}."
