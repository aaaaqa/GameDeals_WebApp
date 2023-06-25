from flask import Blueprint, render_template, request, flash,  redirect, url_for
from flask_login import LoginManager, login_required
from base64 import b64encode
import base64

from models import db, Users, Game, Gamestore, GamestoreGame, IndieGame

review = Blueprint('review', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(review)

@review.route('/review', methods=['GET', 'POST'])
@login_required

def show():
    return render_template('review.html')
