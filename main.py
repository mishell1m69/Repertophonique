from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/apropos')
def apropos():
    return render_template("apropos.html")

@app.route('/ajouter')
def ajouter():
    return render_template("ajouter.html")

@app.route('/modifier')
def modifier():
    return render_template("modifier.html")

@app.route('/supprimer')
def supprimer():
    return render_template("supprimer.html")

@app.route('/howto')
def howto():
    return render_template("howto.html")

@app.route('/rechercher')
def rechercher():
    return render_template("rechercher.html")

@app.route('/add_ppl')
def add_ppl():
    return render_template("add_ppl.html")

@app.route('/add_num')
def add_num():
    return render_template("add_num.html")

@app.route('/add_both')
def add_both():
    return render_template("add_both.html")

@app.route('/added_num')
def added_num():
    return render_template("added_num.html")

app.run(debug=True)
