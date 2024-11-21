from flask import render_template
from modelo.cliente_modelo import ClienteModelo, Cliente

class ClienteController:
    def __init__(self):
        self.modelo = ClienteModelo()
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self):
        self.modelo.agregar_cliente(Cliente(1, "Rodrigo Silva", "rodrigo@example.com", "+56 9 1234 5678"))
        self.modelo.agregar_cliente(Cliente(2, "Maria Lopez", "maria@example.com", "+56 9 8765 4321"))

    def lista_clientes(self):
        clientes = self.modelo.obtener_clientes()
        return render_template('lista_clientes.html', clientes=clientes)

    def detalle_cliente(self, id_cliente):
        cliente = self.modelo.obtener_cliente_por_id(id_cliente)
        if cliente:
            return render_template('detalle_cliente.html', cliente=cliente)
        else:
            return "Cliente no encontrado", 404
