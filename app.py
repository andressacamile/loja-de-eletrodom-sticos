
from flask import Flask, render_template, request
app = Flask(__name__)
minha_loja = loja ()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    nome = request.form['nome']
    endereco = request.form['endereco']
    email = request.form['email']
    minha_loja.cadastrar_cliente(nome, endereco, email)
    return 'Cliente cadastrado com sucesso!'
@app.route('/cadastrar_produto', methods=['POST'])
def cadastrar_produto():
    nome = request.form['nome_produto']
    preco = float(request.form['preco'])
    quantidade = int(request.form['quantidade'])
    minha_loja.cadastrar_produto(nome, preco, quantidade)
    return 'Produto cadastrado com sucesso!'

@app.route('/listar_clientes', methods=['GET'])
def listar_clientes():
    clientes = minha_loja.listar_clientes()
    return render_template('clientes.html', clientes=clientes)

@app.route('/listar_produtos', methods=['GET'])
def listar_produtos():
    produtos = minha_loja.listar_produtos()
    return render_template('produtos.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
