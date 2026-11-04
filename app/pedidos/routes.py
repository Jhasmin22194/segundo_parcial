from flask import Blueprint, render_template, request, redirect, url_for, flash

from ..extensions import db
from ..models import Pedido, Cliente, Producto

bp_pedidos = Blueprint("pedidos", __name__, url_prefix="/pedidos")


def _opciones():
    return Cliente.query.order_by(Cliente.nombre).all(), Producto.query.order_by(Producto.nombre).all()


@bp_pedidos.route("/")
def lista():
    pedidos = Pedido.query.order_by(Pedido.fecha.desc()).all()
    return render_template("pedidos/lista.html", pedidos=pedidos)


@bp_pedidos.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    clientes, productos = _opciones()
    if request.method == "POST":
        cliente = db.session.get(Cliente, int(request.form["cliente_id"]))
        producto = db.session.get(Producto, int(request.form["producto_id"]))
        if producto.stock <= 0:
            flash(f"No hay stock disponible de {producto.nombre}.", "danger")
            return render_template("pedidos/form.html", pedido=None,
                                   clientes=clientes, productos=productos)
        monto = request.form.get("monto", "").strip()
        pedido = Pedido(
            cliente_id=cliente.id,
            producto_id=producto.id,
            monto=float(monto) if monto else producto.precio,
        )
        producto.stock -= 1
        db.session.add(pedido)
        db.session.commit()
        flash("Pedido registrado correctamente.", "success")
        return redirect(url_for("pedidos.lista"))
    return render_template("pedidos/form.html", pedido=None,
                           clientes=clientes, productos=productos)


@bp_pedidos.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    pedido = Pedido.query.get_or_404(id)
    clientes, productos = _opciones()
    if request.method == "POST":
        pedido.cliente_id = int(request.form["cliente_id"])
        pedido.monto = float(request.form["monto"])
        db.session.commit()
        flash("Pedido actualizado", "success")
        return redirect(url_for("pedidos.lista"))
    return render_template("pedidos/form.html", pedido=pedido,
                           clientes=clientes, productos=productos)


@bp_pedidos.route("/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    pedido = Pedido.query.get_or_404(id)
    pedido.producto.stock += 1 
    db.session.delete(pedido)
    db.session.commit()
    flash("Pedido eliminado", "warning")
    return redirect(url_for("pedidos.lista"))
