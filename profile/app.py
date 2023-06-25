"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile')
def profile():
    user = {
        'name': 'FPSLovers',
        'age': 17,
        'location': 'New York',
        'games': [
            {
                'name': 'Game A',
                'image_url': 'static/images/ITT.png'
            },
            {
                'name': 'Game B',
                'image_url': 'static/images/resistance.jpg'
            },
            {
                'name': 'Game C',
                'image_url': 'static/images/bioshockI.jpg'
            }
        ]
    }

    

    return render_template('profile.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
"""