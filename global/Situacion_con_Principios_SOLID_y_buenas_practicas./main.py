from pedido import Pedido
from procesador_pago import ProcesadorPagoTarjeta
from notificador import NotificadorEmail
from repositorio_pedidos import RepositorioPedidos
from gestor_pedidos import GestorPedidos

def main():
    productos = [
        {'nombre': 'Producto 1', 'precio': 50, 'cantidad': 2},
        {'nombre': 'Producto 2', 'precio': 30, 'cantidad': 1}
    ]
 
    cliente = {'nombre': 'Rodrigo', 'email': 'rodrigo@example.com'}
    pedido = Pedido(productos, cliente)
    procesador_pago = ProcesadorPagoTarjeta()
    notificador = NotificadorEmail()
    repositorio = RepositorioPedidos('pedidos.json')
    gestor_pedidos = GestorPedidos(procesador_pago, notificador, repositorio)
 
    gestor_pedidos.procesar_pedido(pedido)
    # Mostrar pedidos guardados
    pedidos_guardados = repositorio.cargar_todos()
    for p in pedidos_guardados:
        print(p.to_dict())

if __name__ == "__main__":
 main()
