from trabajo import Trabajo
from descanso import Descanso

class Desarrollador(Trabajo, Descanso):
    def trabajar(self):
        return "Estoy escribiendo cdigo"
 
    def tomar_descanso(self):
        return "Estoy tomando un descanso"