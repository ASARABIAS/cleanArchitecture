from abc import ABC, abstractmethod

class ProcesadorPago(ABC):
    @abstractmethod
    def procesar(self, monto):
        pass
class ProcesadorPagoTarjeta(ProcesadorPago):
    def procesar(self, monto):
        print(f"Procesando pago de ${monto} con tarjeta de crdito.")
