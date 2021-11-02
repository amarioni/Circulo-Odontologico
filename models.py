from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

# AHORA LA CLASE USER HEREDA LA CLASE MODEL DE SQLALCHEMY
class Profesional(db.Model, UserMixin):
    __tablename__ = 'profesional'
    id = db.Column(db.Integer, primary_key=True)
    id_condicion_fiscal = db.Column(db.Integer(11), nullable=False)
    id_localidad = db.Column(db.Integer(11), nullable=False)
    matricula = db.Column(db.String(11), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    fec_nac = db.Column(db.Date, nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    telefono = db.Column(db.String(14), nullable=False)
    condicion = db.Column(db.Boolean, default=True)

class Paciente(db.Model, UserMixin):  
    __tablename__ = 'paciente'
    id = db.Column(db.Integer(11), primary_key=True)
    id_obra_social_plan = db.Column(db.Integer(11), nullable=False)
    id_localidad = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    fec_nac = db.Column(db.Date, nullable=False)
    n_afiliado = db.Column(db.String(20), nullable=False)
    genero = db.Column(db.Boolean, default=False)
    domicilio = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(14), nullable=False)

class ObrasSocial(db.Model, UserMixin):  
    __tablename__ = 'obra_social'
    id = db.Column(db.Integer(11), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    cuit = db.Column(db.String(15), nullable=False)
    domicilio_postal = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(14), nullable=False)
    condicion = db.Column(db.Boolean, default=True)

class ProfObra(db.Model, UserMixin):
    __tablename__ = 'profesional_obra_social'
    id = db.Column(db.Integer(11), primary_key=True)
    id_obra_social = db.Column(db.Integer(11), nullable=False)
    id_profesional = db.Column(db.Integer(11), nullable=False)
    condicion = db.Column(db.Boolean, default=True)
    
class CondicionFiscal(db.Model, UserMixin):  
    __tablename__ = 'condicion_fiscal'
    id = db.Column(db.Integer(11), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Especialidad(db.Model, UserMixin):  
    __tablename__ = 'especialidad'
    id = db.Column(db.Integer(11), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class ProfEspe(db.Model, UserMixin):
    __tablename__ = 'profesional_especialidad'
    id = db.Column(db.Integer(11), primary_key=True)
    id_profesional = db.Column(db.Integer(11), nullable=False)
    id_especialidad = db.Column(db.Integer(11), nullable=False)

class Localidad(db.Model, UserMixin):  
    __tablename__ = 'localidad'
    id = db.Column(db.Integer(11), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class ObraPlan(db.Model, UserMixin):
    __tablename__ = 'obra_social_plan'
    id = db.Column(db.Integer(11), primary_key=True)
    id_obra_social = db.Column(db.Integer(11), nullable=False)
    id_plan = db.Column(db.Integer(11), nullable=False)

class ObraPractica(db.Model, UserMixin):
    __tablename__ = 'obra_social_practica'
    id = db.Column(db.Integer(11), primary_key=True)
    id_obra_social_plan = db.Column(db.Integer(11), nullable=False)
    id_practica = db.Column(db.Integer(11), nullable=False)

class Plan(db.Model, UserMixin):  
    __tablename__ = 'plan'
    id = db.Column(db.Integer(11), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    cobertura = db.Column(db.Integer(3), nullable=False)

class Practica(db.Model, UserMixin):  
    __tablename__ = 'practica'
    id = db.Column(db.Integer(11), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(6), nullable=False)
    importe = db.Column(db.Integer(9), nullable=False)

class Resumen(db.Model, UserMixin):
    __tablename__ = 'resumen'
    id = db.Column(db.Integer(11), primary_key=True)
    id_paciente = db.Column(db.Integer(11), nullable=False)
    id_profesional_obra_social = db.Column(db.Integer(11), nullable=False)
    importe_total = db.Column(db.Integer(9), nullable=False)
    fecha = db.Column(db.DateTime(), nullable=False)

class DetalleResumen(db.Model, UserMixin):
    __tablename__ = 'detalle_resumen'
    id = db.Column(db.Integer(11), primary_key=True)
    id_obra_social_practica = db.Column(db.Integer(11), nullable=False)
    id_resumen = db.Column(db.Integer(11), nullable=False)
    diente = db.Column(db.Integer(2), nullable=False)
    cara = db.Column(db.String(5), nullable=False)
    cantidad = db.Column(db.Integer(2), nullable=False)

