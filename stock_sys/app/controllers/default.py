from flask import render_template, request, redirect, url_for, flash
from app import app, db

from app.models.forms import CadastroForm, CompraPendenteForm, BuscaForm
from app.models.tables import Produto, CompraPendente


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


##### Gerenciando os produtos #####

@app.route("/adicionar_produto", methods=["GET", "POST"])
def adicionar_produto():
    form = CadastroForm()
    if form.validate_on_submit():
        produtos = Produto(username=request.form['username'], quantidade=request.form['quantidade'],
                           preco_de_venda=request.form['preco_de_venda'], preco_de_compra=request.form['preco_de_compra'])
        db.session.add(produtos)
        db.session.commit()
        return redirect(url_for("lista_produto"))
    return render_template("adicionar_produto.html", form=form)


@app.route("/lista_produto")
def lista_produto():
    produtos = Produto.query.all()
    return render_template("lista_produto.html", produtos=produtos)


@app.route("/atualizar_produto/<int:id>", methods=["GET", "POST"])
@app.route("/atualizar_produto/", methods=["GET", "POST"])
def atualizar_produto(id):
    form = CadastroForm()
    produtos = Produto.query.filter_by(id = id).first()

    if form.validate_on_submit():
        form.populate_obj(produtos)
        db.session.commit()
        return redirect(url_for("lista_produto"))

    form = CadastroForm()
    form.insert_data(produtos)
    return render_template("atualizar_produto.html", form=form, produtos=produtos)

    
@app.route("/excluir_produto/<int:id>")
@app.route("/excluir_produto/", defaults = {"int:id": None})
def excluir_produto(id):
    produtos = Produto.query.filter_by(id = id).first()
    db.session.delete(produtos)
    db.session.commit()
    return redirect(url_for("lista_produto"))


def configure(app):
    app.register_blueprint(app)


##### Busca #####

@app.route("/buscar_produto", methods = ["GET", "POST"])
def buscar_produto():
    form = BuscaForm()
    produto = None
    if form.validate_on_submit():
        busca = busca=request.form['busca']
        produto = Produto.query.filter_by(username = busca).first()
        if produto == None:
            flash("Produto não encontrado")

    return render_template("busca.html", form = form, produto = produto)

    
##### Gerenciando as Compras pendentes #####
    
@app.route('/compra_pendente')
def lista_compra_pendente():
    compras_pendentes = CompraPendente.query.all()
    print(compras_pendentes)
    return render_template('lista_compra_pendente.html', compras_pendentes = compras_pendentes)


@app.route('/add_compra_pendente', methods=["GET", "POST"])
def add_compra_pendente():
    form = CompraPendenteForm()
    if form.validate_on_submit():
        compras_pendentes = CompraPendente(
            nome=request.form['nome'], valor_pendente = request.form['valor_pendente'], dt = request.form['dt'])
        db.session.add(compras_pendentes)
        db.session.commit()
        return redirect(url_for("lista_compra_pendente"))
    return render_template("add_compra_pendente.html", form = form)


@app.route("/atualizar_compra_pendente/<int:id>", methods = ["GET", "POST"])
@app.route("/atualizar_compra_pendente/", methods = ["GET", "POST"])
def atualizar_compra_pendente(id):
    form = CompraPendenteForm()
    compra_pendente = CompraPendente.query.filter_by(id = id).first()

    if form.validate_on_submit():
        form.populate_obj(compra_pendente)
        db.session.commit()
        return redirect(url_for("lista_compra_pendente"))

    form = CompraPendenteForm()
    form.insert_data(compra_pendente)
    return render_template("atualizar_compras_pendentes.html", form = form, compra_pendente=compra_pendente)


@app.route("/excluir_compra_pendente/<int:id>")
@app.route("/excluir_compra_pendente/", defaults = {"int:id": None})
def excluir_compra_pendente(id):
    compra_pendente = CompraPendente.query.filter_by(id = id).first()
    db.session.delete(compra_pendente)
    db.session.commit()
    return redirect(url_for("lista_compra_pendente"))
