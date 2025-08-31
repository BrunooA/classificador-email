from flask import Flask, render_template, request
from dotenv import load_dotenv

import classificador 

app = Flask(__name__)


historico = []

# --- Rotas Flask ---
@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        mensagem = request.form["mensagem"]
        if mensagem != None:
            resultado = classificador.classify_and_respond(mensagem)
            historico.insert(0,resultado) #Insere no começo da lista

    return render_template("index.html",resultados=historico)

    


# if __name__ == "__main__":
#     app.run(debug=True)
