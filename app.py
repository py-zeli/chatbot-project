from flask import Flask

app = Flask(__name__)

@app.route('/endpoint')
def index():
    return 'Olá, mund!'

def conversa():
    return