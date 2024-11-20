class ProductoVista:
    @staticmethod
    def mostrar_productos(productos):
        if productos:
            for producto in productos:
                print(producto)
        else:
            print("No hay productos registrados.")
