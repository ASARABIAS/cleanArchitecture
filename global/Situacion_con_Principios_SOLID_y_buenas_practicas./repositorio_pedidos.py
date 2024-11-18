import json
import os
from pedido import Pedido

class RepositorioPedidos:
    def __init__(self, file_name):
    # Crear la ruta completa al archivo JSON dentro de la carpeta 'data'
        base_dir = os.path.dirname(os.path.dirname(__file__)) 
        # Directorio del proyecto
        self.file_path = os.path.join(base_dir, 'data', file_name)
        # Crear la carpeta 'data' si no existe
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        # Crear el archivo JSON si no existe
        self._asegurar_archivo_json()

    def _asegurar_archivo_json(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)
                print(f"Archivo {self.file_path} creado.")
 
    def guardar(self, pedido):
        with open(self.file_path, 'r') as file:
            pedidos = json.load(file)
            pedidos.append(pedido.to_dict())
        with open(self.file_path, 'w') as file:
            json.dump(pedidos, file, indent=4)
            print(f"Pedido guardado en {self.file_path}")
 
    def cargar_todos(self):
        with open(self.file_path, 'r') as file:
            pedidos_data = json.load(file)
            return [Pedido.from_dict(data) for data in pedidos_data]
