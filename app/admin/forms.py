# HEREDAMOS FLASKFORM
from flask_wtf import FlaskForm
# HEREDAMOS 4 COMPONENTES, CAJA DE TEXTO, BOTON SUBMIT, CAMPO PARA CLAVE y AREA DE TEXTO
from wtforms import StringField, IntegerField, SelectField, SubmitField
# HEREDAMOS VALIDADORES, DATO REQUERIDO, EMAIL Y LARGO DE UN CAMPO
from wtforms.validators import DataRequired, Length

class FileForm(FlaskForm):
    obrasocial = SelectField('Obra Social', validators=[DataRequired()])
    plan = SelectField('Plan', validators=[DataRequired()])
    numafil = IntegerField('Numero de Afiliado', validators=[DataRequired(), Length(max=15, min=1)])
    submit = SubmitField('Siguiente')

class DetailFomr(FlaskForm):
    codigo = SelectField('Codigo', validators=[DataRequired()])
    diente = IntegerField('Diente', validators=[DataRequired(), Length(max=2, min=2)])
    cara = StringField('Nombre del Profesional', validators=[DataRequired(), Length(max=5, min=1)])
    cantidad = IntegerField('Diente', validators=[DataRequired(), Length(max=1, min=1)])
    submit = SubmitField('Guardar')