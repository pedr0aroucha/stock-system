from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
    

class CadastroForm(FlaskForm):
    username = StringField("Nome:", validators=[DataRequired()])
    quantidade = StringField("Quantidade:", validators=[DataRequired()])
    preco_de_venda = StringField(
        "Preço de Venda:", validators=[DataRequired()])
    preco_de_compra = StringField(
        "Preço de Compra:", validators=[DataRequired()])

    def insert_data(self, produtos):
        self.username.data = produtos.username
        self.quantidade.data = produtos.quantidade
        self.preco_de_venda.data = produtos.preco_de_venda
        self.preco_de_compra.data = produtos.preco_de_compra


class CompraPendenteForm(FlaskForm):
    nome = StringField("Nome:", validators=[DataRequired()])
    valor_pendente = StringField(
        "Valor Pendente:", validators=[DataRequired()])
    dt = StringField("Data:", validators=[DataRequired()])

    def insert_data(self, compras_pendentes):
        self.nome.data = compras_pendentes.nome
        self.valor_pendente.data = compras_pendentes.valor_pendente
        self.dt.data = compras_pendentes.dt


class BuscaForm(FlaskForm):
    busca = StringField("Busca:", validators=[DataRequired()])