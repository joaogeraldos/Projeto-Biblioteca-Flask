from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()

# Conteudo da API -- Tabela Livros
class Livros(db.Model):
    __tablename__ = 'livros'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    titulo = db.Column(db.String(100), nullable = False)
    decricao = db.Column(db.String(255), nullable = False)
    sub_titulo = db.Column(db.String(255), nullable = False)
    editora = db.Column(db.String(100))
    tema = db.Column(db.String(100))
    colecao = db.Column(db.String(100))
    numero_pag = db.Column(db.Integer, nullable = False)
    conteudo = db.Column(db.Text, nullable = False)
    img = db.Column(db.LargeBinary)

    def retorno(self):
        return {
            'id':self.id,
            'titulo': self.titulo,
            'decricao': self.decricao,
            'conteudo': self.conteudo,
            'info': self.info
        }

    autor = db.relationship('Autores', back_populates = 'livro', cascade = 'all' )

# Conteudo da API -- Tabela Autores
class Autores(db.Model):
    __tablename__ = 'autores'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(100), nullable = False)
    decricao = db.Column(db.Text, nullable = False)
    img = db.Column(db.LargeBinary)
    livro_id = db.Column(db.Integer, db.ForeignKey('livros.id'), nullable= False)

    livro = db.relationship('Livros', back_populates = 'autor')
    
# Conteudo da API -- Tabela Admin
class Admin(UserMixin, db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(100), nullable = False, unique = True)
    senha = db.Column(db.String(15), nullable = False)

# Conteudo da API -- Tabela Formulario
class Formulario(db.Model):
    __tablename__ = 'formularios'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(100), nullable = False)
    opniao = db.Column(db.Text, nullable = False)