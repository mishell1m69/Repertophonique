from flask import Flask, render_template, request
from Sqlite import *

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

@app.route('/addPpl')
def add_ppl():
    return render_template("addPpl.html")

@app.route('/addNum', methods=['GET', 'POST'])
def add_num():
    return render_template("addNum.html")

@app.route('/addBoth')
def add_both():
    return render_template("addBoth.html")

@app.route('/addNum2', methods=['GET', 'POST'])
def add_num_2():
    if request.method == "POST":
        global first_name,last_name
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        people = people_correspondant([first_name,last_name,None,None])
        
    return render_template("addNum2.html")

@app.route('/addedNum', methods=['GET', 'POST'])
def added_num():

    return render_template("addedNum.html")

app.run(debug=True)