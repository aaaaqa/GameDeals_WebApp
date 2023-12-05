from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user
from base64 import b64encode
from itertools import islice
from sqlalchemy.sql import text
import bs4 as bs
import string
import urllib.request


from models import db, Users, News, Game, GamestoreGame, IndieGame

home = Blueprint('home', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(home)

@home.route('/home', methods=['GET'])
@login_required
def show():
    news_images = db.session.query(News).all()
    image_list = islice([b64encode(img.imageNews).decode('ascii') for img in reversed(news_images)], 0, 3)

    indies_images = db.session.query(IndieGame).first()
    indie_list = [b64encode(indies_images.imageIndie).decode('ascii')]

    my_url = urllib.request.urlopen('https://store.steampowered.com/search/?sort_by=Released_DESC&os=win&supportedlang=english&specials=1&ndl=1').read()

    soup = bs.BeautifulSoup(my_url, 'lxml')
    title_tag = [item.text for item in soup.select('span.title')][:4]
    img_tag = [item['srcset'].split('x, ')[-1].split(' 2x')[0] for item in soup.select('div.col.search_capsule img[srcset]')][:4]
    discount_tag = [item.text for item in soup.select('div.discount_pct')][:4]
    total_tag = [item.text for item in soup.select('div.discount_final_price')][:4]
    parsed_imgs = zip(title_tag, discount_tag, img_tag, total_tag)

    return render_template('home.html', image_list=image_list, list=parsed_imgs, indie_list=indie_list)
    #return render_template('home.html', image_list=image_list, indie_list=indie_list)