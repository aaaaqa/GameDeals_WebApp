from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

newTopic = Blueprint('newTopic', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(newTopic)

@newTopic.route('/newTopic', methods=['GET'])
@login_required
def show():
    return render_template('newTopic.html')
