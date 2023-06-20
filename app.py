import sqlalchemy
from flask_login import LoginManager
from flask import Flask,render_template, request , redirect,url_for

import sys

sys.path.insert(0, './scripts/')

from models import db, Users

from index import index
from login import login
from logout import logout
from register import register
from home import home
from community import community
from profile import profile
from catalog import catalog
from news import news
from newTopic import newTopic

app = Flask(__name__, static_folder='./templates/static')

wishlist = []

def list_append(item):
    global wishlist
    wishlist.append(item)

def list_delete(item):
    global wishlist
    wishlist.remove(item)

@app.route("/",methods = ['GET','POST'])

def main_wishlist():
    if request.method == 'POST':
        item_added = request.form['item']
        if item_added != '':
            list_append(item_added)
        
    return render_template('index.html',wishlist = wishlist)

@app.route("/delete/<item>")

def delete(item):
    list_delete(item)
    return redirect(url_for('main_wishlist'))

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../scripts/database.db'

login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(home)
app.register_blueprint(profile)
app.register_blueprint(community)
app.register_blueprint(catalog)
app.register_blueprint(news)
app.register_blueprint(newTopic)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)