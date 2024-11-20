class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f"Producto(id={self.id_producto}, nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})"
