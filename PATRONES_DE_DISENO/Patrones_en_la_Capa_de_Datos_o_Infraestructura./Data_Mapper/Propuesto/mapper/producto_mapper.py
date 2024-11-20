import json
import os
from entidad.producto import Producto

class ProductoMapper:
    def __init__(self, archivo='productos.json'):
        self.archivo = os.path.join(os.path.dirname(__file__), '..', archivo)

    def _leer_datos(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, 'r') as file:
            productos_dict = json.load(file)
            return [self._from_dict(p) for p in productos_dict]

    def _escribir_datos(self, productos):
        with open(self.archivo, 'w') as file:
            productos_dict = [self._to_dict(producto) for producto in productos]
            json.dump(productos_dict, file, indent=4)

    def agregar_producto(self, producto: Producto):
        productos = self._leer_datos()
        productos.append(producto)
        self._escribir_datos(productos)

    def obtener_todos_los_productos(self):
        return self._leer_datos()

    def obtener_producto_por_id(self, id_producto: int):
        productos = self.obtener_todos_los_productos()
        for producto in productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def actualizar_producto(self, producto_actualizado: Producto):
        productos = self.obtener_todos_los_productos()
        for idx, producto in enumerate(productos):
            if producto.id_producto == producto_actualizado.id_producto:
                productos[idx] = producto_actualizado
                self._escribir_datos(productos)
                return

    def eliminar_producto(self, id_producto: int):
        productos = self.obtener_todos_los_productos()
        productos = [producto for producto in productos if producto.id_producto != id_producto]
        self._escribir_datos(productos)

    def _from_dict(self, producto_dict):
        return Producto(
            id_producto=producto_dict['id_producto'],
            nombre=producto_dict['nombre'],
            precio=producto_dict['precio'],
            cantidad=producto_dict['cantidad']
        )
    
    def _to_dict(self, producto: Producto):
        return {
            'id_producto': producto.id_producto,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'cantidad': producto.cantidad
        }