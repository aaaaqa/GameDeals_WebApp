from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user
from base64 import b64encode
from itertools import islice
from sqlalchemy.sql import text

from models import db, Users, News, Game, GamestoreGame

home = Blueprint('home', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(home)

@home.route('/home', methods=['GET'])
@login_required
def show():
    images = db.session.query(News).all()
    image_list = []
    for img in images:
        image = b64encode(img.imageNews).decode('ascii')
        image_list.append(image)
    image_list = list(islice(reversed(image_list), 0, 3))

    hotsales = db.session.query(Game).all()
    hotsales_list = []
    
    for img in hotsales:
        image = b64encode(img.bannerGame).decode('ascii')
        hotsales_list.append(image)
    hotsales_list = list(islice(reversed(hotsales_list), 0, 6))

    session = db.session()
    discount = session.execute(text('SELECT discountGame FROM Gamestore_Game ORDER BY idGamestoreGame desc LIMIT 6;')).cursor
    discount_list = []

    for d in discount:
        discount_list.append(d[0])

    _list = zip(hotsales_list, discount_list)

    return render_template('home.html', image_list=image_list, list=_list)