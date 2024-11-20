from query.producto_query import ProductoQuery
from entidad.producto import Producto

def main():
    # Crear una instancia de ProductoQuery
    query = ProductoQuery()
    
    # Agregar criterios de filtrado (ejemplo)
    query.filtrar_por_precio(min=10.0, max=50.0)
    query.filtrar_por_stock(min=5)
    
    # Ejecutar la consulta
    productos = query.ejecutar()
    
    # Mostrar los productos filtrados
    for producto in productos:
        print(producto)

if __name__ == "__main__":
    main()
