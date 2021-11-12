
from flask import render_template, redirect, url_for, request, abort
from werkzeug.urls import url_parse
from flask_login import current_user
from app.auth import routes

from . import admin_bp

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

@admin_bp.route('/formfile')
def formfile():
    return render_template('admin/formfile.html')

@admin_bp.route('/formpractices')
def formpractices():
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