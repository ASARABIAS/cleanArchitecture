import json
import os
from entidad.producto import Producto

class UnitOfWork:
    def __init__(self, archivo_productos='productos.json'):
        self.archivo_productos = os.path.join(os.path.dirname(__file__), '..', archivo_productos)
        self.nuevos = []
        self.modificados = []
        self.eliminados = []

    def agregar_nuevo(self, producto: Producto):
        self.nuevos.append(producto)

    def modificar(self, producto: Producto):
        self.modificados.append(producto)

    def eliminar(self, producto: Producto):
        self.eliminados.append(producto)

    def commit(self):
        productos = self._cargar_productos()
        # Aplicar eliminaciones
        for producto in self.eliminados:
            productos = [p for p in productos if p.id_producto != producto.id_producto]
        # Aplicar modificaciones
        for producto in self.modificados:
            for i, p in enumerate(productos):
                if p.id_producto == producto.id_producto:
                    productos[i] = producto
        # Aplicar nuevas inserciones
        productos.extend(self.nuevos)
        self._guardar_productos(productos)
        # Limpiar las listas después de hacer commit
        self.nuevos = []
        self.modificados = []
        self.eliminados = []

    def rollback(self):
        # Simplemente limpiamos las listas de seguimiento
        self.nuevos = []
        self.modificados = []
        self.eliminados = []

    def _cargar_productos(self):
        if not os.path.exists(self.archivo_productos):
            return []
        with open(self.archivo_productos, 'r') as file:
            productos_dict = json.load(file)
            return [Producto.from_dict(p) for p in productos_dict]

    def _guardar_productos(self, productos):
        with open(self.archivo_productos, 'w') as file:
            productos_dict = [p.to_dict() for p in productos]
            json.dump(productos_dict, file, indent=4)
