from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Olá, Sou o Ehxi! ( leia-se Ash! )"