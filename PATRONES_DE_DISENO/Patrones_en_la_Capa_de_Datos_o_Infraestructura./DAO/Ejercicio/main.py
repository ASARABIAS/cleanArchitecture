from dao.producto_dao import ProductoDAO
from entidad.producto import Producto

def ejemplo_uso_dao():
    dao = ProductoDAO()
    
    # 1. Agregar un nuevo producto
    producto1 = Producto(id_producto=1, nombre="Laptop", precio=1200.00, cantidad=10)
    dao.agregar_producto(producto1)
    print("Producto agregado:", producto1)
    
    # 2. Agregar otro producto
    producto2 = Producto(id_producto=2, nombre="Mouse", precio=25.50, cantidad=50)
    dao.agregar_producto(producto2)
    print("Producto agregado:", producto2)
    
    # 3. Obtener todos los productos
    productos = dao.obtener_todos_los_productos()
    print("\nLista de todos los productos:")
    for producto in productos:
        print(producto)
    
    # 4. Actualizar un producto existente
    producto1.precio = 1150.00
    producto1.cantidad = 8
    if dao.actualizar_producto(producto1):
        print("\nProducto actualizado:", producto1)
    
    # 5. Obtener un producto por ID
    producto_encontrado = dao.obtener_producto_por_id(1)
    if producto_encontrado:
        print("\nProducto encontrado por ID:", producto_encontrado)
    
    # 6. Eliminar un producto
    dao.eliminar_producto(2)
    print("\nProducto con ID 2 eliminado.")
    
    # 7. Obtener todos los productos después de la eliminación
    productos = dao.obtener_todos_los_productos()
    print("\nLista de todos los productos después de la eliminación:")
    for producto in productos:
        print(producto)

if __name__ == "__main__":
    ejemplo_uso_dao()
