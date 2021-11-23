from flask import render_template, redirect, url_for, request, abort
from werkzeug.urls import url_parse
from flask_login import current_user
from app.auth import routes

from .import public_bp
from app import public


@public_bp.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('auth.login'))