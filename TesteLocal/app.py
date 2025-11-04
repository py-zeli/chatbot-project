from flask import Flask, request

app = Flask(__name__)

@app.route('/endpoint', methods=['GET','POST'])
def analisar_resposta():
    
    conteudo_requisicao = request.data.decode('utf-8')
    
    print(f"Conteúdo Recebido: '{conteudo_requisicao}'") # Útil para depuração
    
    if "Olá" in conteudo_requisicao:
        resposta = f"Olá, usuário!\nComo posso ajudá-lo?"

        lista_opcoes = """
        1 - Resetar MFA/senha do JumpCloud
        2 - Solicitar acesso a um software
        3 - Problema no Hardware
"""
        return resposta + lista_opcoes
    
    else:
        return "Desculpe, não entendi sua resposta. ;-;"


if __name__ == '__main__':
    app.run(debug=True)