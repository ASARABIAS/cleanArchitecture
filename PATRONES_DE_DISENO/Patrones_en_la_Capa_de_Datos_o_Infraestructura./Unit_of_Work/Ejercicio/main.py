from uow.unit_of_work import UnitOfWork
from entidad.producto import Producto

def ejemplo_uso_uow():
    uow = UnitOfWork()
    
    # 1. Agregar un nuevo producto
    producto1 = Producto(id_producto=1, nombre="Laptop", precio=1200.00, cantidad=10)
    uow.agregar_nuevo(producto1)
    print("Producto preparado para agregar:", producto1)
    
    # 2. Modificar un producto existente
    producto1.precio = 1150.00
    uow.modificar(producto1)
    print("Producto preparado para modificar:", producto1)
    
    # 3. Agregar otro producto
    producto2 = Producto(id_producto=2, nombre="Mouse", precio=25.50, cantidad=50)
    uow.agregar_nuevo(producto2)
    print("Producto preparado para agregar:", producto2)
    
    # 4. Eliminar un producto
    uow.eliminar(producto2)
    print("Producto preparado para eliminar:", producto2)
    
    # 5. Hacer commit de todas las operaciones
    uow.commit()
    print("\nOperaciones aplicadas con éxito.\n")
    
    # 6. Verificar los productos en la base de datos después del commit
    productos = uow._cargar_productos()
    print("Lista de productos después del commit:")
    for producto in productos:
        print(producto)

if __name__ == "__main__":
    ejemplo_uso_uow()

