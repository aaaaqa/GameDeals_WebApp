from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

profile = Blueprint('profile', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(profile)

@profile.route('/profile', methods=['GET'])
@login_required
def show():
    return render_template('profile.html')