from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import login_manager
from . import auth_bp
from .forms import LoginForm
from .models import Usuario, Persona

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    # PRIMERO COMPROBAMOS SI EL USUARIO ESTÁ AUTENTICADO
    if current_user.is_authenticated:
        if current_user.is_admin():
            return redirect(url_for('admin.manager', user_name=current_user.name))
        else:
            return redirect(url_for('admin.professional', user_name=current_user.name))
    form = LoginForm()

    if form.validate_on_submit():
        user = Usuario.get_by_email(form.email.data.upper())
        # SI EXISTE UN USUARIO CON ESE EMAIL Y LA CLAVE ES CORRECTA, 
        # AUTENTICAMOS EL USUARIO USANDO EL METODO login_user
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            # COMPROBAMOS SI RECIBIMOS EL PARAMETRO NEXT. 
            # ESTO PASA CUANDO SE INTENTA INGRESAR A UNA PAGINA PROTEGIDA SIN ESTAR AUTENTICADO.
            # SI NO SE RECIBE EL NEXT, REDIRIGIMOS EL USUARIO A LA PAGINA DE INICIO
            if not next_page or url_parse(next_page).netloc != '':
                if current_user.is_admin():
                    next_page = url_for('admin.manager',user_name=user.name)
                else:
                    next_page = url_for('admin.professional', user_name=user.name)     
            return redirect(next_page)
    return render_template('auth/index.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(int(user_id))
