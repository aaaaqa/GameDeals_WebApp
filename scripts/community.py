from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

community = Blueprint('community', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(community)

@community.route('/community', methods=['GET'])
@login_required
def show():
    return render_template('community.html')
