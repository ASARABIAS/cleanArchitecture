from ave import Ave

class Pinguino(Ave):
    def caminar(self):
        return "Estoy caminando"
    def moverse(self):
        return self.caminar()
