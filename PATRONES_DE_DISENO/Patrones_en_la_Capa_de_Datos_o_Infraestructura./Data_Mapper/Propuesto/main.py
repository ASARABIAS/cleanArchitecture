from entidad.producto import Producto
from mapper.producto_mapper import ProductoMapper

def main():
    mapper = ProductoMapper()

    # Agregar productos
    producto1 = Producto(1, "Laptop", 1200.00, 10)
    producto2 = Producto(2, "Mouse", 25.50, 50)
    mapper.agregar_producto(producto1)
    mapper.agregar_producto(producto2)

    # Listar productos
    productos = mapper.obtener_todos_los_productos()
    for producto in productos:
        print(producto)

    # Actualizar producto
    producto1.precio = 1100.00
    mapper.actualizar_producto(producto1)

    # Eliminar producto
    mapper.eliminar_producto(2)

    # Listar productos después de la eliminación
    productos = mapper.obtener_todos_los_productos()
    for producto in productos:
        print(producto)

if __name__ == "__main__":
    main()
