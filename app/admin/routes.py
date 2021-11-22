
from operator import delitem
from warnings import catch_warnings
from flask import render_template

from datetime import date

from flask.helpers import url_for
from . import admin_bp
from .models import *
from .forms import FileForm, DetailForm

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
    if form.validate_on_submit():
        obrasocial = form.obrasocial.data
        plan = form.plan.data
        numafil = form.numafil.data

        paciente_id = Paciente.get_id(numafil)
        obrasoc_id = obrasocial.id
        prof_obra_soc_id = ProfObra.get_id(obrasoc_id)

        newfile = Resumen(id_paciente=paciente_id.id, id_profesional_obra_social=prof_obra_soc_id.id, importe_total=0, fecha=date.today())
        newfile.save()
<<<<<<< Updated upstream
        return render_template("admin/formpractices.html", form=form)
=======
        return render_template("admin/formpractices.html")
>>>>>>> Stashed changes
    return render_template('admin/formfile.html', form=form)

@admin_bp.route('/formpractices', methods = ['GET','POST'])
def formpractices():
<<<<<<< Updated upstream
    return render_template('admin/formpractices.html')
=======
    form = DetailForm()
    if form.validate_on_submit():
        codigo = form.codigo.data
        diente = form.diente.data
        cara = form.cara.data
        cantidad = form.cantidad.data

        max_id = Resumen.get_max_id()
        practica = Practica.get_id_importe(codigo)

        total = (int(practica.importe) * cantidad)
        importe_cero = Resumen.get_total
        importe_cero.importe_total = total

        newdetail = DetalleRes(id_resumen=max_id, id_practica=practica.id, diente=diente, cara=cara, importe_unitario=practica.importe, cantidad=cantidad )
        newdetail.save
        importe_cero.importe_total.Resumen.Save
        return render_template('admin/profesional.html')
    return render_template('admin/formparactices.html', form=form)
>>>>>>> Stashed changes





