import json
import os

class Pedido:
    def __init__(self, productos, cliente):
        self.productos = productos # Lista de productos en el pedido
        self.cliente = cliente # Cliente que realiza el pedido
 # Aseguramos que el archivo JSON se guarde en el mismo directorio que este archivo Python
        self.file_path = os.path.join(os.path.dirname(__file__), 'pedidos.json')

 # Crear el archivo JSON si no existe
        self._asegurar_archivo_json()
    
    def _asegurar_archivo_json(self):
    # Verificamos si el archivo existe; si no, lo creamos con una lista vaca
 
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)
                print(f"Archivo {self.file_path} creado.")
 
    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto['precio'] * producto['cantidad']
            return total
 
    def enviar_notificacion(self):
        print(f"Enviando notificacin a {self.cliente['email']}: Su pedido ha sido procesado.")
 
    def guardar_en_base_de_datos(self):
        print("Guardando el pedido en la base de datos.")
        # Leer pedidos existentes
        with open(self.file_path, 'r') as file:
            pedidos = json.load(file)
            # Agregar el nuevo pedido a la lista
            pedidos.append({
                'productos': self.productos,
                'cliente': self.cliente
            })
        # Guardar la lista actualizada de pedidos
        with open(self.file_path, 'w') as file:
            json.dump(pedidos, file, indent=4)
            print(f"Pedido guardado en {self.file_path}")
 
    def cargar_pedidos(self):
        try:
            with open(self.file_path, 'r') as file:
                pedidos = json.load(file)
                print(f"Pedidos cargados desde {self.file_path}:")
                for p in pedidos:
                    print(p)
        except FileNotFoundError:
            print(f"No se encontr el archivo {self.file_path}. No se cargaron pedidos.")
 
    def procesar_pago(self):
        print("Procesando el pago.")
        # Cdigo ficticio para procesar el pago
 
    def procesar_pedido(self):
        total = self.calcular_total()
        self.procesar_pago()
        self.guardar_en_base_de_datos()
        self.enviar_notificacion()
        print(f"Pedido procesado. Total: ${total}")
# Ejemplo de uso
if __name__ == "__main__":
    productos = [
        {'nombre': 'Producto 1', 'precio': 50, 'cantidad': 2},
        {'nombre': 'Producto 2', 'precio': 30, 'cantidad': 1}
        ]
    cliente = {'nombre': 'Rodrigo', 'email': 'rodrigo@example.com'}
    pedido = Pedido(productos, cliente)
    pedido.procesar_pedido()
    # Cargar pedidos desde el archivo JSON
    pedido.cargar_pedidos()

