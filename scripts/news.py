from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

news = Blueprint('news', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(news)

@news.route('/news', methods=['GET'])
@login_required
def show():
    return render_template('news.html')
