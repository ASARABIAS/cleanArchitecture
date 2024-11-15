from trabajador import Trabajador

class Gerente(Trabajador):
    def trabajar(self):
        return "Estoy gestionando el equipo"
 
    def tomar_descanso(self):
        return "Estoy tomando un descanso"
 
    def reportar(self):
        return "Estoy reportando el progreso del equipo"