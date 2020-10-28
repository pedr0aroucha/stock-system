from app import db
    

class Produto(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    quantidade = db.Column(db.Integer)
    preco_de_venda = db.Column(db.Integer)
    preco_de_compra = db.Column(db.Integer)

    def __init__(self, username, quantidade, preco_de_venda, preco_de_compra):
        self.username = username
        self.quantidade = quantidade
        self.preco_de_venda = preco_de_venda
        self.preco_de_compra = preco_de_compra

    def __repr(self):
        return "<Produtos %r>" % self.id


class CompraPendente(db.Model):
    __tablename__ = "compras_pendentes"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    valor_pendente = db.Column(db.Integer)
    dt = db.Column(db.Integer)

    def __init__(self, nome, valor_pendente, dt):
        self.nome = nome
        self.valor_pendente = valor_pendente
        self.dt = dt

    def __repr(self):
        return "<Compras Pendentes %r>" % self.id
