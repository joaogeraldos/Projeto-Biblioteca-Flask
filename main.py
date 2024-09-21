from flask import Flask
from API.models import db, Admin
from Rotas.livros import livros_bp
from Rotas.admin import admin_db, LoginManager


app = Flask(__name__, static_folder='base_static')
app.secret_key = 'teste'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api-Livros.db'
db.init_app(app)
lm = LoginManager(app)

@lm.user_loader
def user_loader(id):
    admin = db.session.query(Admin).filter_by(id=id).first()
    return admin


app.register_blueprint(livros_bp)
app.register_blueprint(admin_db)

pass

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)