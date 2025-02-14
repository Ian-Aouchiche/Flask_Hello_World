from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return """<h2>Bonjour tout le monde !</h2>
              <p>Pour accéder à vos exercices cliquez <a href='./exercices/'>Ici</a></p>
              <p>Pour accéder à la page de contact cliquez <a href='./contact/'>Ici</a></p>"""
  
@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')  # Assure-toi que ce fichier existe dans "templates/"

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
