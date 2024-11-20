from controlador.producto_controlador import ProductoControlador

def main():
    controlador = ProductoControlador()
    
    while True:
        opcion = input("Seleccione una opción: 1. Agregar, 2. Listar, 3. Eliminar, 4. Salir\n")
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad en stock: "))
            controlador.agregar_producto(nombre, precio, cantidad)
        elif opcion == "2":
            controlador.listar_productos()
        elif opcion == "3":
            id_producto = int(input("ID del producto a eliminar: "))
            controlador.eliminar_producto(id_producto)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
