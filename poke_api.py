from imports import Flask, request, jsonify, CORS
from controller import Controller  # Supondo que você tenha um controller para interagir com o banco

controller = Controller()

app = Flask(__name__)
CORS(app)

@app.route('/add_pokemon', methods=['POST'])
def add_pokemon():
    # Verifica se os dados necessários foram enviados
    if not request.json or 'nome' not in request.json:
        return jsonify({'error': 'Dados inválidos, campo "nome" obrigatório'}), 400

    # Extraindo dados do corpo da requisição (JSON)
    pokemon_data = {
        'nome': request.json.get('nome'),
        'forca': request.json.get('forca'),
        'resistencia': request.json.get('resistencia'),
        'velocidade': request.json.get('velocidade'),
        'peso': request.json.get('peso'),
        'Shyne': request.json.get('Shyne'),
        'nivel': request.json.get('nivel', 5),  # Se o nível não for passado, assume 5 como padrão
        'fk_Party_id_Party': request.json.get('fk_Party_id_Party'),
        'selvagem': request.json.get('selvagem', True)  # Se 'selvagem' não for passado, assume True
    }

    # Chama o método para inserir no banco de dados (você pode ter uma função para isso)
    result = controller.add_pokemon(pokemon_data)

    if result == 1:
        return jsonify({'message': 'Pokémon adicionado com sucesso!'}), 201
    else:
        return jsonify({'error': 'Erro ao adicionar Pokémon'}), 500

if __name__ == '__main__':
    app.run(debug=True)
