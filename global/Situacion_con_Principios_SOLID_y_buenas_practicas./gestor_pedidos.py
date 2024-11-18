class GestorPedidos:
 
    def __init__(self, procesador_pago, notificador, repositorio):
        self.procesador_pago = procesador_pago
        self.notificador = notificador
        self.repositorio = repositorio
 
    def procesar_pedido(self, pedido):
        total = pedido.calcular_total()
        self.procesador_pago.procesar(total)
        self.repositorio.guardar(pedido)
        self.notificador.enviar("Su pedido ha sido procesado.", pedido.cliente)
        print(f"Pedido procesado. Total: ${total}")