from imports import Flask, request, jsonify, CORS
from controller import Controller  # Supondo que você tenha um controller para interagir com o banco

controller = Controller()

app = Flask(__name__)
CORS(app)

from flask import request, jsonify

# Rota para adicionar um Pokémon
@app.route('/pokemon', methods=['POST'])
def add_pokemon():
    """
    Adiciona um novo Pokémon ao banco de dados.

    Espera que o corpo da requisição esteja no formato JSON contendo os dados do Pokémon.

    Retorna:
        JSON: Mensagem de sucesso ou erro de validação.
    """
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400
    
    params_pokemon = request.json
    controller.add_pokemon(params_pokemon)
    
    return jsonify({'message': 'Pokémon adicionado com sucesso!'}), 201

# Rota para listar Pokémons
@app.route('/pokemon', methods=['GET'])
def list_pokemons():
    """
    Lista os Pokémons cadastrados no banco de dados.

    Parâmetros de consulta (opcionais):
        cols (str): Colunas a serem retornadas, separadas por vírgula. Exemplo: "nome, forca, resistencia".

    Retorna:
        JSON: Lista de Pokémons com as colunas especificadas ou uma mensagem de erro se nenhum Pokémon for encontrado.
    """
    cols = request.args.get('cols', 'nome, forca, resistencia, velocidade, peso, Shyne, nivel, fk_Party_id_Party, selvagem').split(',')
    pokemons = controller.list_pokemons(cols)
    
    if pokemons:
        return jsonify(pokemons), 200
    else:
        return jsonify({'error': 'Nenhum Pokémon encontrado'}), 404

# Rota para deletar um Pokémon
@app.route('/pokemon/<int:id_pokemon>', methods=['DELETE'])
def delete_pokemon(id_pokemon):
    """
    Deleta um Pokémon do banco de dados com base no ID fornecido.

    Parâmetros:
        id_pokemon (int): ID do Pokémon a ser deletado.

    Retorna:
        JSON: Mensagem de sucesso se o Pokémon for deletado ou uma mensagem de erro em caso de falha.
    """
    result = controller.delete_pokemon(id_pokemon)
    
    if result == 1:
        return jsonify({'message': f'Pokémon com ID {id_pokemon} deletado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao deletar Pokémon'}), 500

# Rota para editar um Pokémon
@app.route('/pokemon/<int:id_pokemon>', methods=['PUT'])
def edit_pokemon(id_pokemon):
    """
    Edita os dados de um Pokémon com base no ID fornecido e nos dados enviados no corpo da requisição.

    Parâmetros:
        id_pokemon (int): ID do Pokémon a ser editado.

    Espera que o corpo da requisição esteja no formato JSON com os novos dados do Pokémon.

    Retorna:
        JSON: Mensagem de sucesso se o Pokémon for editado ou uma mensagem de erro em caso de falha.
    """
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400
    
    new_params = request.json
    result = controller.edit_pokemon(id_pokemon, new_params)
    
    if result == 1:
        return jsonify({'message': f'Pokémon com ID {id_pokemon} editado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao editar Pokémon'}), 500

# Rota para adicionar um Treinador
@app.route('/treinador', methods=['POST'])
def add_treinador():
    """
    Adiciona um novo Treinador ao banco de dados.
    
    Espera que o corpo da requisição esteja no formato JSON contendo os dados do Treinador.

    Retorna:
        JSON: Mensagem de sucesso ou erro de validação.
    """
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400

    params_treinador = request.json
    controller.add_treinador(params_treinador)
    
    return jsonify({'message': 'Treinador adicionado com sucesso!'}), 201

# Rota para listar Treinadores
@app.route('/treinador', methods=['GET'])
def list_treinadores():
    """
    Lista Treinadores cadastrados no banco de dados.

    Parâmetros de consulta (opcionais):
        cols (str): Colunas a serem retornadas, separadas por vírgula. Exemplo: "nome, idade, experiencia".

    Retorna:
        JSON: Lista de Treinadores com as colunas especificadas ou uma mensagem de erro se nenhum Treinador for encontrado.
    """
    cols = request.args.get('cols', 'nome, idade, experiencia, fk_party_id').split(',')
    treinadores = controller.list_treinadores(cols)
    
    if treinadores:
        return jsonify(treinadores), 200
    else:
        return jsonify({'error': 'Nenhum Treinador encontrado'}), 404

# Rota para deletar um Treinador
@app.route('/treinador/<int:id_treinador>', methods=['DELETE'])
def delete_treinador(id_treinador):
    """
    Deleta um Treinador do banco de dados com base no ID fornecido.

    Parâmetros:
        id_treinador (int): ID do Treinador a ser deletado.

    Retorna:
        JSON: Mensagem de sucesso se o Treinador for deletado ou uma mensagem de erro em caso de falha.
    """
    result = controller.delete_treinador(id_treinador)
    
    if result == 1:
        return jsonify({'message': f'Treinador com ID {id_treinador} deletado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao deletar Treinador'}), 500

# Rota para editar um Treinador
@app.route('/treinador/<int:id_treinador>', methods=['PUT'])
def edit_treinador(id_treinador):
    """
    Edita os dados de um Treinador com base no ID fornecido e nos dados enviados no corpo da requisição.

    Parâmetros:
        id_treinador (int): ID do Treinador a ser editado.

    Espera que o corpo da requisição esteja no formato JSON com os novos dados do Treinador.

    Retorna:
        JSON: Mensagem de sucesso se o Treinador for editado ou uma mensagem de erro em caso de falha.
    """
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400
    
    new_params = request.json
    result = controller.edit_treinador(id_treinador, new_params)
    
    if result == 1:
        return jsonify({'message': f'Treinador com ID {id_treinador} editado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao editar Treinador'}), 500

if __name__ == '__main__':
    app.run(debug=True)