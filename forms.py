from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, IntegerField,TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired


class AdminForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()], render_kw={'id': 'username', 'placeholder': 'Digite seu username..'})
    senha = StringField('Senha: ', validators=[DataRequired()], render_kw={'id': 'senha', 'placeholder': 'Digite sua senha..'})

    submit = SubmitField('Entrar', render_kw={'id': 'entrar'})

class Adicionar_autor(FlaskForm):
    # Autor
    nome_autor = StringField('Nome: ', validators=[DataRequired()], render_kw={'id': 'nome-autor'})
    descricao_autor = TextAreaField('Descrição: ', validators=[DataRequired()], render_kw={'id': 'desc-autor'})
    img_autor = FileField('Enviar arquivo: ',validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Apenas imagens!')], render_kw={'id': 'img-autor'})

    submit = SubmitField('Publicar', render_kw={'id': 'publicar'})

class Adicionar_dados(FlaskForm):
    #Livros
    titulo = StringField('Titulo: ', validators=[DataRequired()], render_kw={'id': 'titulo'})
    sub_titulo = StringField('Sub_Titulo: ', validators=[DataRequired()], render_kw={'id': 'subtitilo'})
    descricao = TextAreaField('Descrição: ', validators=[DataRequired()], render_kw={'id': 'descricao'})
    editora = StringField('Editora: ', validators=[DataRequired()], render_kw={'id': 'editora'})
    tema = StringField('Tema: ', validators=[DataRequired()], render_kw={'id': 'tema'})
    colecao = StringField('Coleção: ', validators=[DataRequired()], render_kw={'id': 'colecao'})
    paginas = IntegerField('Numeros de paginas: ', validators=[DataRequired()], render_kw={'id': 'pagina'})
    conteudo = TextAreaField('Conteudo: ', validators=[DataRequired()], render_kw={'id': 'conteudo'})
    img = FileField('Enviar arquivo: ',validators=[FileRequired() ,FileAllowed(['jpg', 'png'], 'Apenas imagens!')], render_kw={'id': 'img'})
    autores = FieldList(FormField(Adicionar_autor), min_entries=1)
    
    submit = SubmitField('Publicar', render_kw={'id': 'publicar'})

    