from auto import Auto
from moto import Moto
from camion import Camion
from conductor import Conductor

def main():
    auto = Auto("Toyota", "Corolla", 180, 4)
    moto = Moto("Yamaha", "MT-07", 220, 689)
    camion = Camion("Volvo", "FH16", 140, 25)
    conductor1 = Conductor("Rodrigo")
    conductor2 = Conductor("Maria")
    conductor1.asignar_vehiculo(auto)
    conductor1.conducir()
    conductor1.cargar_combustible(50)
    conductor2.asignar_vehiculo(moto)
    conductor2.conducir()
    conductor2.cargar_combustible(15)
    conductor1.asignar_vehiculo(camion)
    conductor1.conducir()
    conductor1.cargar_combustible(300)

if __name__ == "__main__":
    main()
