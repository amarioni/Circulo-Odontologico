from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref, relationship

from app import db

class Resumen(db.Model):
    __tablename__ = 'resumen'
    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, nullable=False)
    id_profesional_obra_social = db.Column(db.Integer, nullable=False)
    importe_total = db.Column(db.Integer(9), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

class DetalleRes(db.Model):
    __tablename__ = 'detalle_resumen'
    id = db.Column(db.Integer, primary_key=True)
    id_obra_social_practica = db.Column(db.Integer, nullable=False)
    id_resumen = db.Column(db.Integer, nullable=False)
    diente = db.Column(db.Integer(2), nullable=False)
    cara = db.Column(db.String(5), nullable=False)
    diente = db.Column(db.Integer(1), nullable=False)

class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    id_obra_social_plan = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    fec_nac = db.Column(db.Date, nullable=False)
    n_afiliado = db.Column(db.String(20), nullable=False)
    genero = db.Column(db.Boolean, nullable=False)
    domicilio = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(14), nullable=False)

class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Especialidad(db.Model):
    __tablename__ = 'especialidad'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class ProfEsp(db.Model):
    __tablename__ = 'profesional_especialidad'
    id = db.Column(db.Integer, primary_key=True)
    id_profesional = db.Column(db.Integer, nullable=False)
    id_especialidad = db.Column(db.Integer, nullable=False)

class ProfObra(db.Model):
    __tablename__ = 'profesional_obra_social'
    id = db.Column(db.Integer, primary_key=True)
    id_obra_social = db.Column(db.Integer, nullable=False)
    id_profesional = db.Column(db.Integer, nullable=False)
    condicion = db.Column(db.Boolean, nullable=False)

class Profesional(db.Model):
    __tablename__ = 'profesional'
    id = db.Column(db.Integer, primary_key=True)
    id_condicion_fiscal = db.Column(db.Integer, nullable=False)
    id_localidad = db.Column(db.Integer, nullable=False)
    id_persona = db.Column(db.Integer, ForeignKey('persona.id'), nullable=False)
    matricula = db.Column(db.String(11), nullable=False)
    fec_nac = db.Column(db.Date, nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    telefono = db.Column(db.String(14), nullable=False)
    condicion = db.Column(db.Boolean, nullable=False)   

    


class Plan(db.Model):
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    cobertura = db.Column(db.Integer(3), nullable=False)

class ObraSocPlan(db.Model):
    __tablename__ = 'obra_social_plan'
    id = db.Column(db.Integer, primary_key=True)
    id_obra_social = db.Column(db.Integer, nullable=False)
    id_plan = db.Column(db.Integer, nullable=False)

class ObraSoc(db.Model):
    __tablename__ = 'obra_social'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    cuit = db.Column(db.String(15), nullable=False)
    domicilio_postal = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(14), nullable=False)
    condicion = db.Column(db.Boolean, nullable=False)





class ObraSocPractica(db.Model):
    __tablename__ = 'obra_social_practica'
    id = db.Column(db.Integer, primary_key=True)
    id_obra_social_plan = db.Column(db.Integer, nullable=False)
    id_practica = db.Column(db.Integer, nullable=False)

class Practica(db.Model):
    __tablename__ = ''
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(6), nullable=False)
    importe = db.Column(db.Integer(9), nullable=False)