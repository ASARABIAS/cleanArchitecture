import json
import os

class ProductoQuery:
    def __init__(self):
        self.filtros = []

    def filtrar_por_precio(self, min=None, max=None):
        self.filtros.append(lambda p: (min is None or p['precio'] >= min) and (max is None or p['precio'] <= max))
        return self

    def filtrar_por_stock(self, min=None):
        self.filtros.append(lambda p: min is None or p['cantidad'] >= min)
        return self

    def ejecutar(self):
        archivo_productos = os.path.join(os.path.dirname(__file__), '..', 'productos.json')
        with open(archivo_productos, 'r') as f:
            productos = json.load(f)
        
        for filtro in self.filtros:
            productos = list(filter(filtro, productos))
        
        return productos
