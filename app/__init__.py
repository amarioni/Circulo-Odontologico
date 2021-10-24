from flask import Flask
from flask_login import LoginManager
# IMPORTAMOS SQLALCHEMY 
from flask_sqlalchemy import SQLAlchemy
# IMPORTAMOS EL MANEJADOR DE MYSQL
from pymysql import *

login_manager = LoginManager()
# CREAMOS EL OBJETO SQLALCHEMY
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    # LE DECIMOS A LA APP DONDE SE ENCUENTRA LA BASE DE DATOS
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://BD2021:BD2021itec@143.198.156.171/sql_efi_lopezmedina_marioni'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    """
    # Configuración del email
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'mail@gmail.com'
    app.config['MAIL_PASSWORD'] = 'clave'
    app.config['DONT_REPLY_FROM_EMAIL'] = '(Nombre, mail@gmail.com)'
    app.config['ADMINS'] = ('mail@gmail.com', )
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_DEBUG'] = False
    """

    login_manager.init_app(app)
    login_manager.login_view = "login"
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Registro de los Blueprints
    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .manager import manager_bp
    app.register_blueprint(manager_bp)

    from .professional import professional_bp
    app.register_blueprint(professional_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)


    return app

"""
def register_filters(app):
    app.jinja_env.filters['datetime'] = format_datetime

def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404

    @app.errorhandler(401)
    def error_401_handler(e):
        return render_template('401.html'), 401
"""