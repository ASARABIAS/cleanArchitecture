from modelo.producto_modelo import ProductoModelo
from vista.producto_vista import ProductoVista

class ProductoControlador:
    def __init__(self):
        self.modelo = ProductoModelo()
        self.vista = ProductoVista()

    def agregar_producto(self, nombre, precio, cantidad):
        self.modelo.agregar_producto(nombre, precio, cantidad)
        print(f"Producto '{nombre}' agregado con éxito.")

    def listar_productos(self):
        productos = self.modelo.obtener_todos_los_productos()
        self.vista.mostrar_productos(productos)

    def eliminar_producto(self, id_producto):
        self.modelo.eliminar_producto(id_producto)
        print(f"Producto con ID {id_producto} eliminado con éxito.")
