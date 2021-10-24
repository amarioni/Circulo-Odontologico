from flask import Blueprint

professional_bp = Blueprint('professional', __name__, template_folder='templates')

from . import routes