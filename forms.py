# HEREDAMOS FLASKFORM
from flask_wtf import FlaskForm
# HEREDAMOS 4 COMPONENTES, CAJA DE TEXTO, BOTON SUBMIT, CAMPO PARA CLAVE y AREA DE TEXTO
from wtforms import StringField, SubmitField, IntegerField, DateField, BooleanField, SelectField, PasswordField
# HEREDAMOS VALIDADORES, DATO REQUERIDO, EMAIL Y LARGO DE UN CAMPO
from wtforms.validators import DataRequired, Email, Length

class PatientForm(FlaskForm):
    nombre = StringField('Nombre del Profesional', validators=[DataRequired(), Length(max=100)])
    numafil = IntegerField('Numero de Afiliado', validators=[DataRequired(), Length(max=15, min=1)])
    dni = IntegerField('DNI', validators=[DataRequired(), Length(max=9, min=9)])
    fecnac = DateField('Fecha de Nacimiento', format = "%d%m%y", validators=[DataRequired()])
    genero = SelectField('Género', validators=[DataRequired()])
    domicilio = StringField('Domicilio', validators=[DataRequired(), Length(max=100)])
    telefono = IntegerField('Matricula del Profesional', validators=[DataRequired(), Length(max=10, min=8)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Guardar')

class ProfesionalFomr(FlaskForm):
    nombre = StringField('Nombre del Profesional', validators=[DataRequired(), Length(max=100)])
    matricula = IntegerField('Matricula del Profesional', validators=[DataRequired(), Length(max=6, min=6)])
    fecnac = DateField('Fecha de Nacimiento', format = "%d%m%y", validators=[DataRequired()])
    genero = SelectField('Género', validators=[DataRequired()])
    dni = IntegerField('DNI', validators=[DataRequired(), Length(max=9, min=9)])
    direccion = StringField('Dirección', validators=[DataRequired(), Length(max=100)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Guardar')

class FileForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    clave = PasswordField('Contraseña', validators=[DataRequired()])
    recuerdame = BooleanField('Recuérdar mi Cuenta')
    submit = SubmitField('Ingresar')