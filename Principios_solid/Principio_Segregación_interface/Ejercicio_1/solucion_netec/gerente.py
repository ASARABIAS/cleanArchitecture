from trabajo import Trabajo
from descanso import Descanso
from reporte import Reporte

class Gerente(Trabajo, Descanso, Reporte):
    def trabajar(self):
        return "Estoy gestionando el equipo"
 
    def tomar_descanso(self):
        return "Estoy tomando un descanso"
 
    def reportar(self):
        return "Estoy reportando el progreso del equipo"
