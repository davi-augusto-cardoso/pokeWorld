from imports import Flask, request, jsonify, CORS
from controller import Controller  # Supondo que você tenha um controller para interagir com o banco

controller = Controller()

app = Flask(__name__)
CORS(app)

@app.route('/pokemon', methods=['POST'])
def add_pokemon():
    # Verifica se os dados do Pokémon foram enviados no corpo da requisição
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400
    
    # Extrai os parâmetros do Pokémon a partir do corpo da requisição
    params_pokemon = request.json
    
    # Chama o método para adicionar o Pokémon
    controller.add_pokemon(params_pokemon)
    
    return jsonify({'message': 'Pokémon adicionado com sucesso!'}), 201

# Rota para listar Pokémons
@app.route('/pokemon', methods=['GET'])
def list_pokemons():
    # Obtém as colunas desejadas da requisição ou usa todas por padrão
    cols = request.args.get('cols', 'nome, forca, resistencia, velocidade, peso, Shyne, nivel, fk_Party_id_Party, selvagem').split(',')
    
    # Chama o método para listar os Pokémons
    pokemons = controller.list_pokemons(cols)
    
    if pokemons:
        return jsonify(pokemons), 200
    else:
        return jsonify({'error': 'Nenhum Pokémon encontrado'}), 404

# Rota para deletar um Pokémon
@app.route('/pokemon/<int:id_pokemon>', methods=['DELETE'])
def delete_pokemon(id_pokemon):
    # Chama o método para deletar um Pokémon pelo ID
    result = controller.delete_pokemon(id_pokemon)
    
    if result == 1:
        return jsonify({'message': f'Pokémon com ID {id_pokemon} deletado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao deletar Pokémon'}), 500

# Rota para editar um Pokémon
@app.route('/pokemon/<int:id_pokemon>', methods=['PUT'])
def edit_pokemon(id_pokemon):
    # Verifica se os dados do Pokémon foram enviados no corpo da requisição
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400
    
    # Extrai os novos parâmetros do Pokémon
    new_params = request.json
    
    # Chama o método para editar o Pokémon
    result = controller.edit_pokemon(id_pokemon, new_params)
    
    if result == 1:
        return jsonify({'message': f'Pokémon com ID {id_pokemon} editado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao editar Pokémon'}), 500

# Rota para adicionar um Treinador
@app.route('/treinador', methods=['POST'])
def add_treinador():
    # Verifica se os dados do Treinador foram enviados no corpo da requisição
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400

    # Extrai os parâmetros do Treinador a partir do corpo da requisição
    params_treinador = request.json
    
    # Chama o método para adicionar o Treinador
    controller.add_treinador(params_treinador)
    
    return jsonify({'message': 'Treinador adicionado com sucesso!'}), 201

# Rota para listar Treinadores
@app.route('/treinador', methods=['GET'])
def list_treinadores():
    # Obtém as colunas desejadas da requisição ou usa todas por padrão
    cols = request.args.get('cols', 'nome, idade, experiencia, fk_party_id').split(',')
    
    # Chama o método para listar os Treinadores
    treinadores = controller.list_treinadores(cols)
    
    if treinadores:
        return jsonify(treinadores), 200
    else:
        return jsonify({'error': 'Nenhum Treinador encontrado'}), 404

# Rota para deletar um Treinador
@app.route('/treinador/<int:id_treinador>', methods=['DELETE'])
def delete_treinador(id_treinador):
    # Chama o método para deletar um Treinador pelo ID
    result = controller.delete_treinador(id_treinador)
    
    if result == 1:
        return jsonify({'message': f'Treinador com ID {id_treinador} deletado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao deletar Treinador'}), 500

# Rota para editar um Treinador
@app.route('/treinador/<int:id_treinador>', methods=['PUT'])
def edit_treinador(id_treinador):
    # Verifica se os dados do Treinador foram enviados no corpo da requisição
    if not request.json:
        return jsonify({'error': 'Dados inválidos. O corpo da requisição deve estar no formato JSON'}), 400
    
    # Extrai os novos parâmetros do Treinador
    new_params = request.json
    
    # Chama o método para editar o Treinador
    result = controller.edit_treinador(id_treinador, new_params)
    
    if result == 1:
        return jsonify({'message': f'Treinador com ID {id_treinador} editado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Erro ao editar Treinador'}), 500

if __name__ == '__main__':
    app.run(debug=True)