from flask import Flask, request
import json # Importe a biblioteca JSON

app = Flask(__name__)

@app.route('/endpoint', methods=['POST']) # API Gateway do Slack usa POST
def analisar_resposta():
    # 1. Obter o corpo RAW da requisição (como bytes)
    raw_data = request.data
    
    # Verifica se há dados no corpo da requisição
    if not raw_data:
        print("Erro: Corpo da requisição vazio.")
        return "Requisição inválida.", 400

    # 2. Deserializar o JSON para um dicionário Python
    try:
        dados_recebidos = json.loads(raw_data.decode('utf-8'))
    except json.JSONDecodeError:
        print("Erro: Conteúdo não é um JSON válido.")
        return "JSON inválido.", 400

    # 3. Logar a seção 'event' (agora é possível, pois 'dados_recebidos' é um dicionário)
    # Acessa a chave 'event' do dicionário principal.
    slack_event_content = dados_recebidos.get('event', {})

    # 2. Cria variáveis para cada informação necessária, usando o dicionário acima
    user_id = slack_event_content.get('user', 'ID_DESCONHECIDO') 
    conteudo_mensagem = slack_event_content.get('text', '') 
    channel_id = slack_event_content.get('channel', 'CANAL_DESCONHECIDO') 

    # Exemplo de como acessar o user_id:
    print(f"ID do Usuário: {user_id}")

    # 4. Extrair o texto da mensagem do Slack
    # Navegamos até a chave 'text' dentro da seção 'event'
    conteudo_mensagem = slack_event_content.get('text', '') 

    print(f"Texto da Mensagem: '{conteudo_mensagem}'") # Logar o texto extraído
    
    # 5. Aplicar a Lógica
    if "Olá" in conteudo_mensagem:
        # Nota: Retornos devem ser JSON se o cliente esperar JSON
        resposta = f"Olá, usuário!\nComo posso ajudá-lo?"

        lista_opcoes = """
1 - Resetar MFA/senha do JumpCloud
2 - Solicitar acesso a um software
3 - Problema no Hardware
"""
        return resposta + lista_opcoes
    
    # Lidar com a verificação de URL do Slack
    elif dados_recebidos.get('type') == 'url_verification':
        # Deve retornar o 'challenge' para o Slack
        return dados_recebidos.get('challenge')

    else:
        return "Desculpe, não entendi sua resposta. ;-)"


if __name__ == '__main__':
    app.run(debug=True)