from flask import Flask, render_template, request
from Sqlite import *

selected = None

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
        global selected
        first_name = request.form.get("fname") if not request.form.get("fname")=="" else None
        last_name = request.form.get("lname") if not request.form.get("lname")=="" else None
        job = request.form.get("job") if not request.form.get("job")=="" else None
        birth = 2024 - int(request.form.get("age")) if not request.form.get("age")=="" else None
        selected = people_correspondant([first_name,last_name,job,birth])
        if len(selected)>0:
            return render_template("addNum2.html")
        else:
            return render_template("lbozo.html")
    else:
        return render_template("index.html")
        

@app.route('/addedNum', methods=['GET', 'POST'])
def added_num():

    return render_template("addedNum.html")

@app.route('/addedPpl', methods=['GET', 'POST'])
def added_ppl():
    if request.method == "POST":
        global selected
        first_name = request.form.get("fname") if not request.form.get("fname")=="" else None
        last_name = request.form.get("lname") if not request.form.get("lname")=="" else None
        job = request.form.get("job") if not request.form.get("job")=="" else None
        birth = 2024 - int(request.form.get("age")) if not request.form.get("age")=="" else None
        ADD_people([first_name,last_name,job,birth],[None,None,None,None,None])
        
        return render_template("addedPpl.html")
    else:
        return render_template("index.html")

app.run(debug=True)