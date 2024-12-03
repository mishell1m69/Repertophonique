from flask import Flask, render_template, request

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

@app.route('/addedNum', methods=['GET', 'POST'])
def added_num():
    if request.method == "POST":
        global first_name,last_name
        first_name = request.form.get("fname")
        last_name = request.form.get("lname") 
        print("Your name is", first_name, last_name)
    return render_template("addedNum.html")

app.run(debug=True)
