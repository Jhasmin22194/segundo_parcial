from datetime import datetime
from .extensions import db
class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    pedidos = db.relationship("Pedido", backref="producto", lazy=True, cascade="all, delete-orphan")
    def __repr__(self):return f"<Producto {self.nombre}>"
class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    pedidos = db.relationship("Pedido", backref="cliente", lazy=True,
                              cascade="all, delete-orphan")
    def __repr__(self): return f"<Cliente {self.nombre}>"
class Pedido(db.Model):
    __tablename__ = "pedidos"
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.now)
    monto = db.Column(db.Float, nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    def __repr__(self): return f"<Pedido {self.id}>"