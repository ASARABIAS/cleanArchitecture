from modelo.producto_modelo import ProductoModelo

class ProductoController:
    def __init__(self):
        self.modelo = ProductoModelo()

    def agregar_producto(self, nombre, precio, cantidad):
        self.modelo.agregar_producto(nombre, precio, cantidad)

    def obtener_todos_los_productos(self):
        return self.modelo.obtener_todos_los_productos()

    def eliminar_producto(self, id_producto):
        self.modelo.eliminar_producto(id_producto)
