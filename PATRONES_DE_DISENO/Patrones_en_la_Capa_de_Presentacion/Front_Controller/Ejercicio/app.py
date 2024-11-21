from flask import Flask, request, redirect, url_for
from controladores.cliente_controller import ClienteController
from controladores.admin_controller import AdminController

app = Flask(__name__)

# Instancias de los controladores
cliente_controller = ClienteController()
admin_controller = AdminController()

# Confección del Front Controller
class FrontController:
    def manejar_solicitud(self, path):
        if path == "" or path == "clientes":
            return cliente_controller.lista_clientes()
        elif path.startswith("cliente/"):
            id_cliente = int(path.split("/")[1])
            return cliente_controller.detalle_cliente(id_cliente)
        elif path == "admin/dashboard":
            return admin_controller.dashboard()
        elif path == "admin/configuraciones":
            return admin_controller.configuraciones()
        else:
            return "Página no encontrada", 404

# Instancia del Front Controller
front_controller = FrontController()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def manejar_ruta(path):
    return front_controller.manejar_solicitud(path)

if __name__ == '__main__':
    app.run(debug=True)
