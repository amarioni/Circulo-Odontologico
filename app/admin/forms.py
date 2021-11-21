# HEREDAMOS FLASKFORM
from flask_wtf import FlaskForm
# HEREDAMOS 4 COMPONENTES, CAJA DE TEXTO, BOTON SUBMIT, CAMPO PARA CLAVE y AREA DE TEXTO
from wtforms import StringField, IntegerField, SubmitField
# HEREDAMOS VALIDADORES, DATO REQUERIDO, EMAIL Y LARGO DE UN CAMPO
from wtforms.validators import DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectField #para lista desplegable
from .models import *

class FileForm(FlaskForm):
    obrasocial = QuerySelectField(query_factory=ObraSoc.obrasoc_query, allow_blank=True, get_label='nombre')
    plan = QuerySelectField(query_factory=Plan.plan_query, allow_blank=True, get_label='nombre')
    numafil = StringField('Numero de Afiliado', validators=[DataRequired(), Length(max=15, min=1)])
    submit = SubmitField('Siguiente')

class DetailFomr(FlaskForm):
    codigo = QuerySelectField('Codigo', validators=[DataRequired()])
    diente = IntegerField('Diente', validators=[DataRequired(), Length(max=2, min=2)])
    cara = StringField('Nombre del Profesional', validators=[DataRequired(), Length(max=5, min=1)])
    cantidad = IntegerField('Diente', validators=[DataRequired(), Length(max=1, min=1)])
    submit = SubmitField('Guardar')

class PatientName(object):
    nombre = StringField('Nombre del Paciente', validators=[DataRequired(), Length(50)])
    submit = SubmitField()
