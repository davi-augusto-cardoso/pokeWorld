from imports import Flask, request, jsonify, CORS, send_from_directory
from controller import Controller

controller = Controller()

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('pages', 'index.html')

@app.route('/pages/<path:filename>')
def static_files(filename):
    return send_from_directory('pages', filename)

@app.route('/pages/src/<path:filename>')
def images(filename):
    return send_from_directory('pages/src', filename)

# Rotas para Pokémon
@app.route('/pokemon', methods=['POST'])
def add_pokemon():
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400

    params_pokemon = request.json
    controller.add_pokemon(params_pokemon)
    return jsonify({'message': 'Pokémon adicionado com sucesso!'}), 201

@app.route('/pokemon', methods=['GET'])
def list_pokemons():
    cols = request.args.get('cols', 'Id_pokemon, nome, forca, resistencia, velocidade, peso, shyne, nivel, fk_party_id_Party, selvagem').split(',')
    pokemons = controller.list_pokemons(cols)

    if pokemons:
        return jsonify(pokemons), 200
    else:
        return jsonify({'error': 'Nenhum Pokémon encontrado'}), 404

@app.route('/pokemon/<int:id_pokemon>', methods=['DELETE'])
def delete_pokemon(id_pokemon):
    result = controller.delete_pokemon(id_pokemon)
    if result:
        return jsonify({'message': f'Pokémon com ID {id_pokemon} deletado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao deletar Pokémon'}), 500

@app.route('/pokemon/<int:id_pokemon>', methods=['PUT'])
def edit_pokemon(id_pokemon):
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400

    new_params = request.json
    result = controller.edit_pokemon(id_pokemon, new_params)

    if result == 1:
        return jsonify({'message': f'Pokémon com ID {id_pokemon} editado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao editar Pokémon'}), 500

# Rotas para Treinador
@app.route('/treinador', methods=['POST'])
def add_treinador():
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400

    params_treinador = request.json
    controller.add_trainer(params_treinador)
    return jsonify({'message': 'Treinador adicionado com sucesso!'}), 201

@app.route('/treinador', methods=['GET'])
def list_treinadores():
    cols = request.args.get('cols', 'nome, data_nasc, genero, CPF').split(',')
    treinadores = controller.list_trainer(cols)  # Corrigido o nome da função para `list_trainer`

    if treinadores:
        return jsonify(treinadores), 200
    else:
        return jsonify({'error': 'Nenhum Treinador encontrado'}), 404

@app.route('/treinador/<int:id_treinador>', methods=['DELETE'])
def delete_treinador(id_treinador):
    result = controller.delete_treinador(id_treinador)
    if result == 1:
        return jsonify({'message': f'Treinador com ID {id_treinador} deletado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao deletar Treinador'}), 500

@app.route('/treinador/<int:id_treinador>', methods=['PUT'])
def edit_treinador(id_treinador):
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400

    new_params = request.json
    result = controller.edit_treinador(id_treinador, new_params)

    if result == 1:
        return jsonify({'message': f'Treinador com ID {id_treinador} editado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao editar Treinador'}), 500

# Rota para Listar Party
@app.route('/party/<int:id_treinador>', methods=['GET'])
def list_party(id_treinador):
    cols = request.args.get('cols', 'id_party, fk_Treinador_ID_treinador, fk_Pokemon_Id_pokemon').split(',')
    party = controller.list_party(id_treinador)

    if party:
        return jsonify(party), 200
    else:
        return jsonify({'error': 'Nenhuma party encontrada'}), 404


@app.route('/shyne', methods=['POST'])
def add_shyne():
    if not request.json or 'pokemon_id' not in request.json or 'is_shiny' not in request.json:
        return jsonify({'error': 'Dados inválidos. É necessário enviar pokemon_id e is_shiny no formato JSON'}), 400

    pokemon_id = request.json['pokemon_id']
    is_shiny = request.json['is_shiny']
    
    result = controller.add_shyne(pokemon_id, is_shiny)
    if result == 1:
        return jsonify({'message': f'Status shiny para o Pokémon com ID {pokemon_id} adicionado com sucesso!'}), 201
    else:
        return jsonify({'error': 'Erro ao adicionar status shiny'}), 500

# Rota para obter o status shiny de um Pokémon
@app.route('/shyne/<int:pokemon_id>', methods=['GET'])
def get_shyne(pokemon_id):
    result = controller.get_shyne(pokemon_id)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': f'Status shiny para o Pokémon com ID {pokemon_id} não encontrado'}), 404

# Rota para atualizar o status shiny de um Pokémon
@app.route('/shyne/<int:pokemon_id>', methods=['PUT'])
def update_shyne(pokemon_id):
    if not request.json or 'is_shiny' not in request.json:
        return jsonify({'error': 'Dados inválidos. É necessário enviar is_shiny no formato JSON'}), 400

    is_shiny = request.json['is_shiny']
    result = controller.update_shyne(pokemon_id, is_shiny)
    
    if result == 1:
        return jsonify({'message': f'Status shiny para o Pokémon com ID {pokemon_id} atualizado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao atualizar status shiny'}), 500

# Rota para deletar o status shiny de um Pokémon
@app.route('/shyne/<int:pokemon_id>', methods=['DELETE'])
def delete_shyne(pokemon_id):
    result = controller.delete_shyne(pokemon_id)
    if result == 1:
        return jsonify({'message': f'Status shiny para o Pokémon com ID {pokemon_id} deletado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao deletar status shiny'}), 500
if __name__ == '__main__':
    app.run(debug=True)
