from flask import Flask

app = Flask(__name__)

@app.route('/')

# função para carregar o que mostra no browser, baseado na rota que passei (app.route)
def home():
    return "Hello, world!"

app.run(port=5000)