from almacenamiento_archivo import AlmacenamientoArchivo

class ProcesadorOrdenes:
    def __init__(self):
        self.almacenamiento = AlmacenamientoArchivo()

    def procesar(self, orden):
        # Lgica de procesamiento
        print(f"Procesando la orden: {orden}")
        self.almacenamiento.guardar_orden(orden)
