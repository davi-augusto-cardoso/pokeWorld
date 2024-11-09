from utils import CRUD
from imports import json

class Controller:
    
    def __init__(self):
        self.__crud = CRUD()
        self.__crud.open_connection()
    
    # POKEMON 
    def add_pokemon(self, params_pokemon:dict):
        self.__crud.create('pokemon',  
                            list(params_pokemon.keys()), 
                            list(params_pokemon.values()))
    
    def list_pokemons(self, cols:tuple)->dict:
        return self.__crud.read('pokemon', cols)
    
    def delete_pokemon(self, id_pokemon:int):
        self.__crud.delete('pokemon', 'Id_pokemon', id_pokemon)
    
    def edit_pokemon(self, id_pokemon:int, new_params:dict):
        self.__crud.update('pokemon', new_params, 'Id_pokemon', id_pokemon)
    
    # TREINADOR
    def add_trainer(self, params_treinador:dict):
        print(params_treinador)
        self.__crud.create('treinador', 
                           list(params_treinador.keys()),
                           list(params_treinador.values()))
        
    def list_trainer(self, cols:tuple)->dict:
        return self.__crud.read('treinador', cols)
    
    def delete_treinador(self, id_treiandor:int):
        self.__crud.delete('treinador', 'Id_treinador', id_treiandor)

    def edit_treinador(self, id_treiandor:int, new_params:dict):
        self.__crud.update('treinador', new_params, 'Id_treinador', id_treiandor)

    # PARTY
    def add_party(self, id_treinador:int, id_pokemon:int):
        id_party = self.__crud.read('party', ('id_party'), {'fk_Treinador_ID_treinador' : id_treinador})
        
        self.edit_pokemon(id_pokemon, { 'fk_Party_id_Party'  :   list(id_party.values())[0],
                                        'selvagem'  :   False})


    def list_party(self, idTreinador)->dict:
        id_party = self.__crud.read('party', ('id_party'), {'fk_Treinador_ID_treinador' : idTreinador})
        return self.__crud.read('pokemon',{'fk_Party_id_Party' : id_party})
    
    def add_shyne(self, pokemon_id: int, is_shiny: bool) -> int:
        """Adiciona um status shiny a um Pokémon."""
        params_shyne = {
            'fk_Pokemon_Id_pokemon': pokemon_id,
            'is_shiny': is_shiny
        }
        return self.__crud.create('Shyne', list(params_shyne.keys()), list(params_shyne.values()))
    
    def get_shyne(self, pokemon_id: int) -> dict:
        """Obtém o status shiny de um Pokémon."""
        result = self.__crud.read('Shyne', ('fk_Pokemon_Id_pokemon', 'is_shiny'), {'fk_Pokemon_Id_pokemon': pokemon_id})
        return json.loads(result) if result != -1 else None
    
    def update_shyne(self, pokemon_id: int, is_shiny: bool) -> int:
        """Atualiza o status shiny de um Pokémon."""
        return self.__crud.update('Shyne', {'is_shiny': is_shiny}, 'fk_Pokemon_Id_pokemon', pokemon_id)
    
    def delete_shyne(self, pokemon_id: int) -> int:
        """Remove o status shiny de um Pokémon."""
        return self.__crud.delete('Shyne', 'fk_Pokemon_Id_pokemon', pokemon_id)