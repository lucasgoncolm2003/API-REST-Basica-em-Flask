from flask import Flask, jsonify, request
app = Flask(__name__)
livros = [
    {'id': 1,'título': 'O Senhor dos Anéis - A Sociedade do Anel','autor': 'J.R.R. Tolkien'},
    {'id': 2,'título': 'Harry Potter e a Pedra Filosofal','autor': 'J.K. Rowling'},
    {'id': 3,'título': 'Hábitos Atômicos','autor': 'James Clear'}
]

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json() # Recebe Informação do Usuário
    for indice,livro in enumerate(livros): # Enumerar os Livros
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route('/livros',methods=['POST'])
def incluir_livro():
    livro_add = request.get_json()
    livros.append(livro_add)
    return livros

@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro_por_id(id):
    for indice,livro in enumerate(livros): # Enumerar os Livros
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)
