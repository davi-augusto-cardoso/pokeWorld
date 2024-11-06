from utils import CRUD
from imports import json

class Controller:
    
    def __init__(self):
        self.__crud = CRUD()
        self.__crud.open_connection()
    
    def add_pokemon(self, params_pokemon):
        self.__crud.create('pokemon',  
                            list(params_pokemon.keys()), 
                            list(params_pokemon.values()))
    
    def list_pokemons(self, cols:tuple):
        return self.__crud.read('pokemon', cols)
    
    def delete_pokemon(self, id_pokemon):
        self.__crud.delete('pokemon', 'Id_pokemon', id_pokemon)
    
    def edit_pokemon(self, id_pokemon:int, new_params:dict):
        self.__crud.update('pokemon', new_params, 'Id_pokemon', id_pokemon)
    
    def add_trainer(self, params_treinador):
        self.__crud.create('treinador', list(params_treinador.values()))
        
    
    
controller = Controller()

pikachu = {
    "nome": "Pikachu",
    # "Id_pokemon": "NULL",
    "forca": "55",
    "resistencia": "40",
    "velocidade": "90",
    "peso": "6.0",
    "Shyne": False,
    "nivel": "5",
    "fk_Party_id_Party": None,
    "selvagem": True
}
bulbasaur = {
    "nome": "Bulbasaur",
    "forca": "49",
    "resistencia": "49",
    "velocidade": "45",
    "peso": "6.9",
    "Shyne": False,
    "nivel": "5",
    "fk_Party_id_Party": None,
    "selvagem": True
}

charmander = {
    "nome": "Charmander",
    "forca": "52",
    "resistencia": "43",
    "velocidade": "65",
    "peso": "8.5",
    "Shyne": False,
    "nivel": "5",
    "fk_Party_id_Party": None,
    "selvagem": True
}

squirtle = {
    "nome": "Squirtle",
    "forca": "48",
    "resistencia": "65",
    "velocidade": "43",
    "peso": "9.0",
    "Shyne": False,
    "nivel": "5",
    "fk_Party_id_Party": None,
    "selvagem": True
}

jigglypuff = {
    "nome": "Jigglypuff",
    "forca": "45",
    "resistencia": "20",
    "velocidade": "20",
    "peso": "5.5",
    "Shyne": False,
    "nivel": "5",
    "fk_Party_id_Party": None,
    "selvagem": True
}

meowth = {
    "nome": "Meowth",
    "forca": "45",
    "resistencia": "35",
    "velocidade": "90",
    "peso": "4.2",
    "Shyne": True,
    "nivel": "5",
    "fk_Party_id_Party": None,
    "selvagem": True
}

new_pikachu = {
    "nome": "Pikachu",
    # "Id_pokemon": "NULL",
    "forca": "90",
    "resistencia": "90",
    "velocidade": "180",
    "peso": "6.0",
    "Shyne": False,
    "nivel": "5",
    "fk_Party_id_Party": None,
    "selvagem": True
}


# set_clause = ', '.join([f"{col[0]} = {col[1]}" for col in new_pikachu.items()])
# print(set_clause)
# pokemons_list = controller.list_pokemons()
# print(pokemons_list)

# controller.edit_pokemon(2, new_pikachu)

# pokemons_list = controller.list_pokemons()
# print(pokemons_list)

print('aõ')