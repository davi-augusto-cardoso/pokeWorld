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
        self.__crud.create('treinador', list(params_treinador.values()))
        
    def list_trainer(self, cols:tuple)->dict:
        return self.__crud.read('treinador', cols)
    
    def delete_pokemon(self, id_treiandor:int):
        self.__crud.delete('treinador', 'Id_treinador', id_treiandor)

    def edit_treinador(self, id_treiandor:int, new_params:dict):
        self.__crud.update('treinador', new_params, 'Id_treinador', id_treiandor)

    # PARTY
    def add_party(self, id_treinador:int, id_pokemon:int):
        id_party = self.__crud.read('party', ('id_party'), {'fk_Treinador_ID_treinador' : id_treinador})
        
        self.edit_pokemon(id_pokemon, { 'fk_Party_id_Party'  :   list(id_party.values())[0],
                                        'selvagem'  :   False})


