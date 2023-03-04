from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Olá, Sou o Ehxi! ( leia-se Ash! )"

if __name__ == '__main__':
    app.run()
    