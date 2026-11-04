from app import create_app
from app.extensions import db
from app.models import Producto, Cliente, Pedido

app = create_app()

with app.app_context():
    if Producto.query.count() == 0:
        productos = [
            Producto(nombre="Laptop Lenovo IdeaPad", precio=4200.00, stock=10),
            Producto(nombre="Mouse inalámbrico Logitech", precio=120.00, stock=50),
            Producto(nombre="Teclado mecánico", precio=350.00, stock=25),
            Producto(nombre="Monitor 24 pulgadas", precio=1300.00, stock=8),
            Producto(nombre="Audífonos Bluetooth", precio=280.00, stock=30),
        ]
        clientes = [
            Cliente(nombre="Jhasmin Catacora Ticona", telefono="70123456"),
            Cliente(nombre="Sonia Ticona Maydana", telefono="71234567"),
            Cliente(nombre="Esther Rocio Charata Catacora", telefono="72345678"),
            Cliente(nombre="Anibal Corini Apaza", telefono="73456789"),
            Cliente(nombre="Alina Quispe Mita", telefono="73567890"),
        ]
        db.session.add_all(productos + clientes)
        db.session.commit()

        pedidos = [
            Pedido(cliente_id=clientes[0].id, producto_id=productos[0].id, monto=productos[0].precio),
            Pedido(cliente_id=clientes[1].id, producto_id=productos[1].id, monto=productos[1].precio),
            Pedido(cliente_id=clientes[2].id, producto_id=productos[3].id, monto=productos[3].precio),
            Pedido(cliente_id=clientes[4].id, producto_id=productos[4].id, monto=productos[4].precio),
            Pedido(cliente_id=clientes[0].id, producto_id=productos[0].id, monto=productos[0].precio),
            Pedido(cliente_id=clientes[1].id, producto_id=productos[1].id, monto=productos[1].precio),
            Pedido(cliente_id=clientes[4].id, producto_id=productos[3].id, monto=productos[3].precio),
            Pedido(cliente_id=clientes[3].id, producto_id=productos[4].id, monto=productos[4].precio),
        ]
        for p in pedidos:
            db.session.get(Producto, p.producto_id).stock -= 1
        db.session.add_all(pedidos)
        db.session.commit()
        print("Datos de prueba cargados.")
    else:
        print("La base de datos ya tiene datos.")
