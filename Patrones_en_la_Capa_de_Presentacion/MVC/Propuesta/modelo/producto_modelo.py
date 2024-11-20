class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f"Producto(id={self.id_producto}, nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})"

class ProductoModelo:
    def __init__(self):
        self.productos = []
        self.id_counter = 1

    def agregar_producto(self, nombre, precio, cantidad):
        producto = Producto(self.id_counter, nombre, precio, cantidad)
        self.productos.append(producto)
        self.id_counter += 1

    def obtener_todos_los_productos(self):
        return self.productos

    def eliminar_producto(self, id_producto):
        self.productos = [producto for producto in self.productos if producto.id_producto != id_producto]
