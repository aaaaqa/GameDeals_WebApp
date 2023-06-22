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
    if request.method == 'POST':
        file = request.files['inputFile']
        data = file.read()
        render_pic = base64.b64encode(data).decode('ascii') 
        render_file = render_pic
        newFile = IndieGame(
                        imageIndie=data, 
                        rendered_data=render_file)
        db.session.add(newFile)
        db.session.commit() 
        #flash(f'Pic {newFile.nameGame} uploaded Text: {newFile.descriptionGame}')
        return redirect(url_for('home.show') + '?success=image-uploaded')
    return render_template('review.html')