from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Definindo a rota para aceitar métodos GET (mostrar form) e POST (processar form)
@app.route('/login', methods=['GET', 'POST'])
def login():
    # --- INÍCIO DA CONDICIONAL ---
    # 1. Verifica se o método da requisição é POST (o usuário enviou o formulário)
    if request.method == 'POST':
        # Pega os dados enviados pelo formulário
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        # 2. SEGUNDA CONDICIONAL: Verifica as credenciais
        if usuario == 'admin' and senha == '12345':
            # Se as credenciais estiverem corretas, redireciona para outra página
            # Usamos o redirect e url_for para enviar o usuário para a rota 'sucesso'
            return redirect(url_for('sucesso', nome=usuario))
        else:
            # Se a senha estiver incorreta
            mensagem = "Erro: Usuário ou senha inválidos."
            # Retorna o formulário novamente, mas com uma mensagem de erro
            return render_template_string(FORMULARIO_HTML, mensagem=mensagem)
            
    # 3. ELSE (Condição implícita: Se o método NÃO é POST, ele é GET)
    else:
        # Se for GET, apenas mostra o formulário vazio
        mensagem = "Por favor, faça login."
        return render_template_string(FORMULARIO_HTML, mensagem=mensagem)
    # --- FIM DA CONDICIONAL ---

@app.route('/sucesso/<nome>')
def sucesso(nome):
    return f"<h1>Login realizado com sucesso!</h1><p>Bem-vindo, {nome}.</p>"


# --- HTML BÁSICO (Para simplificar, usando render_template_string) ---
FORMULARIO_HTML = """
<!doctype html>
<title>Login</title>
<h1>{{ mensagem }}</h1>
<form method="POST" action="/login">
    <p><input name="usuario" placeholder="Usuário"></p>
    <p><input name="senha" type="password" placeholder="Senha"></p>
    <p><input type="submit" value="Entrar"></p>
</form>
"""

if __name__ == '__main__':
    app.run(debug=True)