from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

catalog = Blueprint('catalog', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(catalog)

@catalog.route('/catalog', methods=['GET'])
@login_required
def show():
    return render_template('catalog.html')
