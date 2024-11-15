from procesador_ordenes import ProcesadorOrdenes
from almacenamiento_archivo import AlmacenamientoArchivo

# Uso
if __name__ == "__main__":
    almacenamiento = AlmacenamientoArchivo()
    procesador = ProcesadorOrdenes(almacenamiento)
    procesador.procesar("Orden #1")
