from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref, relationship, session

from app import db

class Resumen(db.Model):
    __tablename__ = 'resumen'
    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id', ondelete='CASCADE'), nullable=False)
    id_profesional_obra_social = db.Column(db.Integer, db.ForeignKey('profesional_obra_social.id', ondelete='CASCADE'), nullable=False)
    importe_total = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    def resumen_query():
        return Resumen.query

    def save(self): #este sirve para grabar en la base de datos un nuevo resumen
        db.session.add(self)
        db.session.commit()

class DetalleRes(db.Model):
    __tablename__ = 'detalle_resumen'
    id = db.Column(db.Integer, primary_key=True)
    id_resumen = db.Column(db.Integer, db.ForeignKey('resumen.id', ondelete='CASCADE'), nullable=False)
    id_practica = db.Column(db.Integer, db.ForeignKey('practica.id', ondelete='CASCADE'), nullable=False)
    diente = db.Column(db.Integer,  nullable=False)
    cara = db.Column(db.String(5), nullable=False)
    importe_unitario = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def detalleres_query():
        return DetalleRes.query

class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    id_obra_social_plan = db.Column(db.Integer, db.ForeignKey('obra_social_plan.id', ondelete='CASCADE'), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    fec_nac = db.Column(db.Date, nullable=False)
    n_afiliado = db.Column(db.String(20), nullable=False)
    genero = db.Column(db.Boolean, nullable=False)
    domicilio = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(14), nullable=False)

    #def get_id(n_afiliado):
    #    return session.query(Paciente.id).filter(Paciente.n_afiliado == n_afiliado)

    def get_id(n_afiliado):
        return Paciente.query.filter_by(n_afiliado=n_afiliado).first()

    def paciente_query():
        return Paciente.query

class Especialidad(db.Model):
    __tablename__ = 'especialidad'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def especialidad_query():
        return Especialidad.query

class ProfEsp(db.Model):
    __tablename__ = 'profesional_especialidad'
    id = db.Column(db.Integer, primary_key=True)
    id_profesional = db.Column(db.Integer, db.ForeignKey('profesional.id', ondelete='CASCADE'), nullable=False)
    id_especialidad = db.Column(db.Integer, db.ForeignKey('especialidad.id', ondelete='CASCADE'), nullable=False)

    def profesp_query():
        return ProfEsp.query

class ProfObra(db.Model):
    __tablename__ = 'profesional_obra_social'
    id = db.Column(db.Integer, primary_key=True)
    id_obra_social = db.Column(db.Integer, db.ForeignKey('obra_social.id', ondelete='CASCADE'), nullable=False)
    id_profesional = db.Column(db.Integer, db.ForeignKey('profesional.id', ondelete='CASCADE'), nullable=False)
    condicion = db.Column(db.Boolean, nullable=False)

    def profobra_query():
        return ProfObra.query

    #def get_id(id_obra_social):
    #    return session.query(ProfObra.id).filter(ProfObra.id_obra_social == id_obra_social)

    def get_id(id_obra_social):
        return ProfObra.query.filter_by(id_obra_social=id_obra_social).first()

class Plan(db.Model):
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    cobertura = db.Column(db.Integer, nullable=False)
    
    def plan_query(): #new
        return Plan.query

class ObraSocPlan(db.Model):
    __tablename__ = 'obra_social_plan'
    id = db.Column(db.Integer, primary_key=True)
    id_obra_social = db.Column(db.Integer, db.ForeignKey('obra_social.id', ondelete='CASCADE'), nullable=False)
    id_plan = db.Column(db.Integer, db.ForeignKey('plan.id', ondelete='CASCADE'), nullable=False)

    def obrasocplan_query():
        return ObraSocPlan.query

class ObraSoc(db.Model):
    __tablename__ = 'obra_social'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    cuit = db.Column(db.String(15), nullable=False)
    domicilio_postal = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(14), nullable=False)
    condicion = db.Column(db.Boolean, nullable=False)

    def obrasoc_query(): #new
        return ObraSoc.query

    #def get_id(nombre):
    #    return session.query(ObraSoc.id).filter(ObraSoc.nombre == nombre)

    def get_id(nombre):
        return ObraSoc.query.filter_by(nombre=nombre).first()

class ObraSocPractica(db.Model):
    __tablename__ = 'obra_social_practica'
    id = db.Column(db.Integer, primary_key=True)
    id_obra_social_plan = db.Column(db.Integer, db.ForeignKey('obra_social_plan.id', ondelete='CASCADE'), nullable=False)
    id_practica = db.Column(db.Integer, db.ForeignKey('practica.id', ondelete='CASCADE'), nullable=False)

    def obrasocpractica_query():
        return ObraSocPractica.query

class Practica(db.Model):
    __tablename__ = ''
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(6), nullable=False)
    importe = db.Column(db.Integer, nullable=False)

    def practica_query():
        return Practica.query