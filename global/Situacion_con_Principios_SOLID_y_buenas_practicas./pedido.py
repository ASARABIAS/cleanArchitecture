class Pedido:
    def __init__(self, productos, cliente):
        self.productos = productos
        self.cliente = cliente
 
    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto['precio'] * producto['cantidad']
        return total
 
    def to_dict(self):
        return {
            'productos': self.productos,
            'cliente': self.cliente
        }
 
    @staticmethod
    def from_dict(data):
        return Pedido(data['productos'], data['cliente'])