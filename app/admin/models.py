from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey

from sqlalchemy.orm import backref, relationship

from app import db

class Resumen(db.Model):
    __tablename__ = 'resumen'
    id = db.Column(db.Integer, primary_key=True)
    id_tipo_usuario = db.Column(db.Integer(), nullable=False)
    id_persona = db.Column(db.Integer, ForeignKey('persona.id'), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)