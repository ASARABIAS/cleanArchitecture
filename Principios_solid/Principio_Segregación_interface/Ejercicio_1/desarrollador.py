from trabajador import Trabajador

class Desarrollador(Trabajador):
    def trabajar(self):
        return "Estoy escribiendo cdigo"
 
    def tomar_descanso(self):
        return "Estoy tomando un descanso"
 
    def reportar(self):
        # Este mtodo no es relevante para Desarrollador, pero debe implementarlo
        return "Reportando trabajo" # removerlo de la interfaz y que sea propio de gerente
