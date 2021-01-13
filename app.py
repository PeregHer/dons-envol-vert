from flask import Flask, render_template, request, redirect, url_for, flash
from atlas import Connexion

app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/don", methods=('GET', 'POST'))
def don():
    if request.method == 'POST':
            prenom = request.form['prenom']
            nom = request.form['nom']
            email = request.form['email']
            telephone = request.form['telephone']
            montant = request.form['montant']

            if not prenom:
                flash('Veuillez entrer votre prénom!')
            elif not nom:
                flash('Veuillez entrer votre nom!')
            elif not email:
                flash('Veuillez entrer votre email!')
            elif not telephone:
                flash('Veuillez entrer votre téléphone!')
            elif not montant:
                flash('Veuillez entrer le montant de votre don!')
            else:
                Connexion.insert(prenom, nom, email, telephone, montant)
                return redirect(url_for('index'))
    return render_template('don.html')

@app.route("/donateurs")
def donateurs():
    posts = Connexion.get_dons()
    return render_template('donateurs.html', posts=posts)

@app.route("/admin", methods=('GET', 'POST'))
def admin():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user == 'admin' and password == 'admin':
            return render_template('admin.html')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)