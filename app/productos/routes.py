from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models import Producto
bp_productos = Blueprint("productos", __name__)
@bp_productos.route("/")
def lista():
    productos = Producto.query.order_by(Producto.id).all()
    return render_template("productos/lista.html", productos=productos)
@bp_productos.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        try:
            producto = Producto(
                nombre=request.form["nombre"].strip(),
                precio=float(request.form["precio"]),
                stock=int(request.form["stock"]),
            )
        except ValueError:
            flash("Precio y stock deben ser numéricos.", "danger")
            return render_template("productos/form.html", producto=None)
        db.session.add(producto)
        db.session.commit()
        flash("Producto creado correctamente", "success")
        return redirect(url_for("productos.lista"))
    return render_template("productos/form.html", producto=None)

@bp_productos.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    producto = Producto.query.get_or_404(id)
    if request.method == "POST":
        try:
            producto.nombre = request.form["nombre"].strip()
            producto.precio = float(request.form["precio"])
            producto.stock = int(request.form["stock"])
        except ValueError:
            flash("Precio y stock deben ser numéricos", "danger")
            return render_template("productos/form.html", producto=producto)
        db.session.commit()
        flash("Producto actualizado", "success")
        return redirect(url_for("productos.lista"))
    return render_template("productos/form.html", producto=producto)

@bp_productos.route("/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash("Producto eliminado", "warning")
    return redirect(url_for("productos.lista"))
