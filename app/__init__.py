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

    app.config['SECRET_KEY'] = 'c74d9b911e14474f9beb8d15f0765410'
    # LE DECIMOS A LA APP DONDE SE ENCUENTRA LA BASE DE DATOS
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://BD2021:BD2021itec@143.198.156.171:3306/sql_efi_lopezmedina_marioni'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    login_manager.login_view = "login"
    
    db.init_app(app)

    # Registro de los Blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)


    return app