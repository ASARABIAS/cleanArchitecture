from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje, cliente):
        pass
    
class NotificadorEmail(Notificador):
    def enviar(self, mensaje, cliente):
        print(f"Enviando email a {cliente['email']}: {mensaje}")

