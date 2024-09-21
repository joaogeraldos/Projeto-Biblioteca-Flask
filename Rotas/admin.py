from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from API.models import db, Admin, Livros, Autores
from forms import AdminForm, Adicionar_dados
from werkzeug.utils import secure_filename


import hashlib

admin_db = Blueprint('admin', __name__)

def hash(txt):
    hash_obj = hashlib.sha256(txt.encode('utf-8'))
    return hash_obj.hexdigest()


@admin_db.route('/admin_cadastro', methods = ['GET', 'POST'])
def cadastro_admin():
    form = AdminForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            senha = form.senha.data

            novo_user = Admin(username=username, senha=hash(senha))
            db.session.add(novo_user)
            db.session.commit()

            return redirect(url_for('admin.deshboard'))

    return render_template('./pages/admin.html', form=form)


@admin_db.route('/login_admin', methods = ['GET', 'POST'])
def login():
    form = AdminForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            senha = form.senha.data

            user = db.session.query(Admin).filter_by(username=username, senha=hash(senha)).first()

            if not user:
                return redirect(url_for('admin.login'))
            
            login_user(user)

            return redirect(url_for('admin.deshboard'))

    elif request.method == 'GET':
        return render_template('./pages/login.html', form=form)


@admin_db.route('/deshboard', methods = ['GET', 'POST'])
# @login_required
def deshboard():
    if request.method == 'GET':
        livro = db.session.query(Livros)
        titulo = ''
        for i in livro:
            titulo = i.titulo
        nome_user = current_user
        return render_template('./pages/deshboard.html', titulo=titulo, nome = nome_user)
    elif request.method == 'POST':

        return redirect(url_for('admin.adicionar'))

@admin_db.route('/adicionar', methods = ['GET', 'POST'])
# @login_required
def adicionar():
    form = Adicionar_dados()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            print('Livro salvo no banco de dados')
            #Livro
            img = form.img.data 
            filename = secure_filename(img.filename)

            novo_livro = Livros(
                titulo = form.titulo.data,
                decricao = form.descricao.data,
                sub_titulo = form.sub_titulo.data,
                editora = form.editora.data,
                tema =  form.tema.data,
                colecao = form.colecao.data,
                numero_pag = form.paginas.data,
                conteudo = form.conteudo.data,
                img = img.read(),  
            )

            for autor_form in form.autores:
                file = autor_form.img_autor.data
                filename = secure_filename(file.filename)
                autor = Autores (
                    nome = autor_form.nome_autor.data,
                    decricao = autor_form.descricao_autor.data,
                    img = file.read(),
                    livro = novo_livro
                )
                db.session.add(autor)
            
            db.session.add(novo_livro)
            db.session.commit()
            return redirect(url_for('admin.deshboard'))
        else:
            print(form.errors)

    return render_template('pages/adicionar.html', form=form)


@admin_db.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.login'))