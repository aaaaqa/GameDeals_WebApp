from flask import Flask,render_template, request , redirect,url_for

app = Flask(__name__)
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

app.run(debug=True)