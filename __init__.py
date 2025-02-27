from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """<h2>Bonjour tout le monde !</h2>
              <p>Pour accéder à vos exercices cliquez <a href='/exercices/'>Ici</a></p>
              <p>Pour accéder à la page de contact cliquez <a href='/contact/'>Ici</a></p>
              <p>Pour accéder à la page du carré cliquez <a href='/calcul_carre/'>Ici</a></p>
              <p>Pour accéder à la page somme cliquez <a href='/somme/'>Ici</a></p>
              <p>Pour accéder à la page somme de tout cliquez <a href='/sommedetout/'>Ici</a></p>
              <p>Pour accéder à la page max de tout cliquez <a href='/max/'>Ici</a></p>
              <p>Pour accéder à la page du cnam cliquez <a href='/cnam/'>Ici</a></p>
              <p>Pour accéder à la page exercice1 cliquez <a href='/exercice_base1/'>Ici</a></p>
              <p>Pour accéder à la page exercice2 cliquez <a href='/exercice_base2/'>Ici</a></p>
              <p>Pour accéder à la page exercice3 cliquez <a href='/exercice_base3/'>Ici</a></p>
              <p>Pour accéder au formulaire cliquez <a href='/formulaire/'>Ici</a></p>
              <p><a href='/actualite/'>Lien vers l'actualité</a></p>
              <p>Pour accéder à page1 cliquez <a href='/page1/'>Ici</a></p>
              <p>Pour accéder à page2 cliquez <a href='/page2/'>Ici</a></p>
              <p>Pour accéder à page3 cliquez <a href='/page3/'>Ici</a></p>
              <p>Pour accéder à CV cliquez <a href='/CV/'>Ici</a></p>
              <p>Pour accéder à maison cliquez <a href='/maison/'>Ici</a></p>
              <p>Pour accéder à maison cliquez <a href='/valet/'>Ici</a></p>"""






@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return f"<h2>Le carré de votre valeur est : {val_user * val_user}</h2>"

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    resultat = valeur1 + valeur2
    parite = "pair" if resultat % 2 == 0 else "impair"
    return f"<h2>La somme des valeurs est : {resultat}</h2><p>Le nombre est {parite}.</p>"

@app.route('/sommedetout/<path:valeurs>')
def somme_de_tout(valeurs):
    liste_valeurs = list(map(int, valeurs.split('/')))
    resultat = sum(liste_valeurs)
    valeurs_str = " + ".join(map(str, liste_valeurs))  
    return f"<h2>La somme de {valeurs_str} est : {resultat}</h2>"

@app.route('/max/<path:valeurs>')
def valeur_max(valeurs):
    liste_valeurs = list(map(int, valeurs.split('/')))
    max_valeur = max(liste_valeurs)
    return f"<h2>La valeur maximale est : {max_valeur}</h2>"

@app.route('/cnam/')
def afficher_cnam():
    return render_template('cnam.html')

@app.route('/exercice_base1/')
def exercice_base1():
    return render_template('1_Liste_Base.html')

@app.route('/exercice_base2/')
def exercice_base2():
    return render_template('exercice_base2.html')

@app.route('/exercice_base3/')
def exercice_base3():
    return render_template('exercice_base3.html')

@app.route('/formulaire/')
def formulaire():
    return render_template('formulaire.html')

@app.route('/page1/')
def page1():
    return render_template('TD1_page1.html')

@app.route('/actualite/')
def actualite():
    return render_template('actualite.html')

@app.route('/page2/')
def page2():
    return render_template('TD1_page2.html')

@app.route('/page3/')
def page3():
    return render_template('TD1_page3.html')

@app.route('/CV/')
def CV():
    return render_template('TD1_CV.html')

@app.route('/maison/')
def maison():
    return render_template('maison.html')

@app.route('/valet/')
def valet():
    return render_template('valet.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
