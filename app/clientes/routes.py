from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models import Cliente
bp_clientes = Blueprint("clientes", __name__, url_prefix="/clientes")
@bp_clientes.route("/")
def lista():
    clientes = Cliente.query.order_by(Cliente.id).all()
    return render_template("clientes/lista.html", clientes=clientes)
@bp_clientes.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        cliente = Cliente(
            nombre=request.form["nombre"].strip(),
            telefono=request.form["telefono"].strip(),
        )
        db.session.add(cliente)
        db.session.commit()
        flash("Cliente creado correctamente", "success")
        return redirect(url_for("clientes.lista"))
    return render_template("clientes/form.html", cliente=None)
@bp_clientes.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == "POST":
        cliente.nombre = request.form["nombre"].strip()
        cliente.telefono = request.form["telefono"].strip()
        db.session.commit()
        flash("Cliente actualizado", "success")
        return redirect(url_for("clientes.lista"))
    return render_template("clientes/form.html", cliente=cliente)


@bp_clientes.route("/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente eliminado", "warning")
    return redirect(url_for("clientes.lista"))
