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

    steam_url_to_scrape = 'https://store.steampowered.com/search/?sort_by=Released_DESC&os=win&supportedlang=english&specials=1&ndl=1'

    parsed_imgs = scrapeHotSales(steam_url_to_scrape)

    return render_template('home.html', image_list=image_list, list=parsed_imgs, indie_list=indie_list)

def scrapeHotSales(url):
    try:
        with urllib.request.urlopen(url) as response:
            my_url = response.read()

        soup = bs.BeautifulSoup(my_url, 'lxml')

        title_tags = [item.text for item in soup.select('span.title')][:4]
        discount_tags = [item.text for item in soup.select('div.discount_pct')][:4]
        img_tags = [item['srcset'].split('x, ')[-1].split(' 2x')[0] for item in soup.select('div.col.search_capsule img[srcset]')][:4]
        total_tags = [item.text for item in soup.select('div.discount_final_price')][:4]
        link_tags = [link['href'] for link in soup.find_all('a', {'class': ['search_result_row', 'ds_collapse_flag', 'app_impression_tracked']})][:4]
        
        return zip(title_tags, discount_tags, img_tags, total_tags, link_tags)
    except Exception as e:
        print(f"An error ocurred: {e}")
        return None