from almacenamiento import Almacenamiento

class AlmacenamientoArchivo(Almacenamiento):
    def guardar_orden(self, orden):
        with open('ordenes.txt', 'a') as f:
            f.write(f"{orden}\n")