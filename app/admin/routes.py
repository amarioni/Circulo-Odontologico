from datetime import date

from flask import render_template, redirect, request
from flask.helpers import url_for

from . import admin_bp
from .forms import FileForm, DetailForm
from .models import *


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


@admin_bp.route('/formfile', methods=['GET', 'POST'])
def formfile():
    form = FileForm()
    if form.validate_on_submit():
        obrasocial = form.obrasocial.data
        numafil = form.numafil.data
        paciente_id = Paciente.get_id(numafil)
        obrasoc_id = obrasocial.id
        prof_obra_soc_id = ProfObra.get_id(obrasoc_id)

        newfile = Resumen(
            id_paciente=paciente_id.id,
            id_profesional_obra_social=prof_obra_soc_id.id,
            importe_total=0,
            fecha=date.today())
        newfile.save()
        return redirect(url_for("admin.formpractices", resumen_id=newfile.id))
    return render_template('admin/formfile.html', form=form)


@admin_bp.route('/formpractices', methods=['GET', 'POST'])
def formpractices():
    resumen= request.args.get('resumen_id')
    resumen_id = Resumen.get(resumen)
    form_detalle = DetailForm()
    if form_detalle.validate_on_submit():
        codigo = form_detalle.codigo.data
        diente = form_detalle.diente.data
        cara = form_detalle.cara.data
        cantidad = form_detalle.cantidad.data

        total = int(codigo.importe * cantidad)
        resumen.importe_total = total
        resumen.save()

        newdetail = DetalleRes(
            id_resumen=resumen_id,
            id_practica=codigo.id,
            diente=diente,
            cara=cara,
            importe_unitario=codigo.importe,
            cantidad=cantidad)
        newdetail.save()
        
        return render_template('admin/profesional.html')
    return render_template("admin/formpractices.html", resumen_id=resumen_id, form_detalle=form_detalle)
