from flask import Blueprint, render_template

index = Blueprint('index', __name__, template_folder='../templates')

@index.route('/index', methods=['GET'])
def show():
    return render_template('index.html')