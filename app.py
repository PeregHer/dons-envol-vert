from flask import Flask, render_template, request, redirect, url_for
from atlas import Connexion

app = Flask(__name__)

@app.route('/')
def index():
    montant = Connexion.get_sum()
    return render_template('index.html', montant=montant)

@app.route("/don", methods=('GET', 'POST'))
def don():
    if request.method == 'POST':
        prenom = request.form['prenom']
        nom = request.form['nom']
        email = request.form['email']
        telephone = request.form['telephone']
        montant = request.form['montant']
        Connexion.insert(prenom, nom, email, telephone, montant)
        return redirect(url_for('index'))
    
    return render_template('don.html')

@app.route("/donateurs")
def donateurs():
    dons = Connexion.get_dons()
    return render_template('donateurs.html', dons=dons)

@app.route("/admin", methods=('GET', 'POST'))
def admin():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user == 'admin' and password == 'admin':
            return render_template('admin.html')
    return render_template('login.html')

@app.route("/conditions")
def conditions():
    return render_template('conditions.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)