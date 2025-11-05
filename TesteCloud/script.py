import json

def lambda_handler(event, context):
    """
    Função Handler da AWS Lambda para processar uma requisição HTTP.

    :param event: O objeto de evento JSON passado pela fonte (ex: API Gateway).
    :param context: O objeto de contexto do runtime da Lambda.
    :return: Uma resposta formatada para o API Gateway.
    """
    # 1. Extrair o corpo (body) da requisição HTTP
    # O API Gateway envia o corpo da requisição como uma string dentro de event['body'].
    
    # O corpo da requisição (body) costuma ser uma string JSON.
    request_body_string = event.get('body')

    if not request_body_string:
        # Lidar com requisições sem corpo (ou payloads inválidos)
        return {
            'statusCode': 400,
            'body': json.dumps({'erro': 'Corpo da requisição ausente ou inválido.'})
        }

    # 2. Deserializar o corpo (transformar a string JSON em dicionário Python)
    try:
        dados_recebidos = json.loads(request_body_string)
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'erro': 'Corpo da requisição não é um JSON válido.'})
        }
        
    # Presumindo que o valor que você quer analisar está na chave 'conteudo'
    conteudo_requisicao = dados_recebidos.get('conteudo', '')
    
    # 3. Aplicar a Lógica Solicitada
    resposta_mensagem = ""
    if conteudo_requisicao == "Olá":
        resposta_mensagem = "Oi"
    elif conteudo_requisicao == "Tchau":
        resposta_mensagem = "Adeus"
    else:
        # Opcional: lidar com outros conteúdos
        resposta_mensagem = f"Não entendi a mensagem: {conteudo_requisicao}" 

    # 4. Formatar a Resposta para o API Gateway
    # O API Gateway espera um dicionário com 'statusCode', 'headers' e 'body' (como string JSON)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps({
            'mensagem_recebida': conteudo_requisicao,
            'resposta_lambda': resposta_mensagem
        })
    }
# Agora vai!!!