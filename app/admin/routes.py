
from flask import render_template, redirect, url_for, request, abort
from werkzeug.urls import url_parse

from datetime import date
from . import admin_bp
from .models import *
from .forms import *

@admin_bp.route('/manager')
def manager():
    
    return render_template('admin/manager.html')

@admin_bp.route('/professional')
def professional():
    return render_template('admin/professional.html')

@admin_bp.route('/formprofesional')
def formprofessional():
    return render_template('admin/formprofessional.html')

@admin_bp.route('/formpatient')
def formpatient():
    return render_template('admin/formpatient.html')

@admin_bp.route('/formfile', methods = ['GET','POST'])
def formfile():
    form = FileForm()
    if form.validate_on_submit:
        obrasocial = form.obrasocial.data
        plan = form.plan.data
        numafil = form.numafil.data

        paciente_id = Paciente.get_id(numafil)
        obrasoc_id = ObraSoc.get_id(obrasocial)
        prof_obra_soc_id = ProfObra.get_id(obrasoc_id)

        newfile = Resumen(id_paciente=paciente_id, id_profecional_obras_social=prof_obra_soc_id, importe_total=0, fecha=date.today())
        newfile.save()
        return render_template("admin/formfile.html", form=form)
    return render_template('admin/formfile.html', form=form)

@admin_bp.route('/formpractices')
def formpractices():
    render_template('admin/formpractices.html')
    """
    if s None:
        abort(404)
    return render_template('admin/formpractices.html')
"""
"""
def register_error_handlers(app):

    @admin_bp.errorhandler(500)
    def base_error_handler(e):
        return render_template('admin/500.html'), 500

    @admin_bp.errorhandler(404)
    def error_404_handler(e):
        return render_template('admin/404.html'), 404

"""