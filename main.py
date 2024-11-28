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
@app.route('/leprojet')
def leprojet():
    return render_template("leprojet.html")
app.run(debug=True)
