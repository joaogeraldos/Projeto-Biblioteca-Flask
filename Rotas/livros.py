from flask import Blueprint, jsonify, request
from API.models import db, Livros

livros_bp = Blueprint('livros', __name__)

@livros_bp.route('/livros', methods = ['GET', 'POST'])
def livros():
    if request.method == 'POST':
        data = request.get_json()
        livros = Livros(titulo= data['titulo'], decricao=data['decricao'], conteudo = data['conteudo'], info = data['info'])
        db.session.add(livros)
        db.session.commit()
        return jsonify({'menssage': 'Livro cadastrado com sucesso'})


    livro = db.session.query(Livros)
    teste = [i.retorno() for i in livro]
    return jsonify(teste)
