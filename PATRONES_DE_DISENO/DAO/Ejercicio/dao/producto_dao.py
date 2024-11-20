import json
import os
from entidad.producto import Producto

class ProductoDAO:
    def __init__(self, archivo_productos='productos.json'):
        self.archivo_productos = os.path.join(os.path.dirname(__file__), '..', archivo_productos)

    def cargar_productos(self):
        if not os.path.exists(self.archivo_productos):
            return []
        with open(self.archivo_productos, 'r') as file:
            productos_dict = json.load(file)
            return [Producto.from_dict(p) for p in productos_dict]

    def guardar_productos(self, productos):
        with open(self.archivo_productos, 'w') as file:
            productos_dict = [producto.to_dict() for producto in productos]
            json.dump(productos_dict, file, indent=4)

    def agregar_producto(self, producto: Producto):
        productos = self.cargar_productos()
        productos.append(producto)
        self.guardar_productos(productos)

    def obtener_todos_los_productos(self):
        return self.cargar_productos()

    def obtener_producto_por_id(self, id_producto: int):
        productos = self.cargar_productos()
        for producto in productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def actualizar_producto(self, producto_actualizado: Producto):
        productos = self.cargar_productos()
        for i, producto in enumerate(productos):
            if producto.id_producto == producto_actualizado.id_producto:
                productos[i] = producto_actualizado
                self.guardar_productos(productos)
                return True
        return False

    def eliminar_producto(self, id_producto: int):
        productos = self.cargar_productos()
        productos = [producto for producto in productos if producto.id_producto != id_producto]
        self.guardar_productos(productos)
