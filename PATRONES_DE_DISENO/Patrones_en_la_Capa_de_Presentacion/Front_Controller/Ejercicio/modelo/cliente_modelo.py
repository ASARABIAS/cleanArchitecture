class Cliente:
    def __init__(self, id_cliente: int, nombre: str, email: str, telefono: str):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"Cliente {self.id_cliente}: {self.nombre} - Email: {self.email}, Teléfono: {self.telefono}"

class ClienteModelo:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def obtener_clientes(self):
        return self.clientes

    def obtener_cliente_por_id(self, id_cliente: int):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
