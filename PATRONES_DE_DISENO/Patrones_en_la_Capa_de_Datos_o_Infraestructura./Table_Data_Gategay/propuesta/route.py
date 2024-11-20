from flask import Flask, request, jsonify
from gateway.producto_gateway import ProductoGateway
from entidad.producto import Producto

app = Flask(__name__)
gateway = ProductoGateway()

@app.route('/productos', methods=['POST'])
def agregar_producto():
    datos = request.json
    nombre = datos.get('nombre')
    precio = datos.get('precio')
    cantidad = datos.get('cantidad')
    id_producto = gateway.obtener_todos_los_productos()[-1].id_producto + 1 if gateway.obtener_todos_los_productos() else 1
    producto = Producto(id_producto, nombre, precio, cantidad)
    gateway.agregar_producto(producto)
    return jsonify({'producto': producto.to_dict()}), 201

@app.route('/productos', methods=['GET'])
def listar_productos():
    productos = gateway.obtener_todos_los_productos()
    productos_dict = [producto.to_dict() for producto in productos]
    return jsonify({'productos': productos_dict})

@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    datos = request.json
    nueva_cantidad = datos.get('cantidad')
    producto = gateway.obtener_producto_por_id(id)
    if producto:
        producto.actualizar_stock(nueva_cantidad)
        gateway.actualizar_producto(producto)
        return jsonify({'producto': producto.to_dict()})
    else:
        return jsonify({'mensaje': 'Producto no encontrado'}), 404

@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    if gateway.eliminar_producto(id):
        return jsonify({'mensaje': f'Producto con ID {id} eliminado.'})
    else:
        return jsonify({'mensaje': 'Producto no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
