from flask import Flask, render_template, request
from dotenv import load_dotenv

import classificador 

app = Flask(__name__)


resultados = []

# --- Rotas Flask ---
@app.route("/", methods=["POST","GET"])
def index():
    result = None
    response_text = None
    email_text = ""
    if request.method == "POST":
        email_text = request.form["email_text"]
        if email_text != None:
            resultado = classificador.classify_and_respond(email_text)
            resultados.append(resultado)

        print(resultados)

    resultados.reverse()
    return render_template("index.html",resultados=resultados)

    

if __name__ == "__main__":
    app.run(debug=True)
