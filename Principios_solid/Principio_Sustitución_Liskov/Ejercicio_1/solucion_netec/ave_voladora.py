from ave import Ave

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    def moverse(self):
        return self.volar()