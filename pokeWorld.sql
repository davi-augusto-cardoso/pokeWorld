DROP DATABASE IF EXISTS pokemon;
CREATE DATABASE pokemon;
USE pokemon;

/* Tabela de Regiões */
CREATE TABLE Regiao (
    nome VARCHAR(20),
    ID_regial INT PRIMARY KEY
);

/* Tabela de Pokémon */
CREATE TABLE Pokemon (
    nome VARCHAR(20) NOT NULL,
    Id_pokemon INT PRIMARY KEY AUTO_INCREMENT,
    forca INT NOT NULL,
    resistencia INT NOT NULL,
    velocidade INT NOT NULL,
    peso FLOAT NOT NULL,
    nivel INT DEFAULT 5,
    fk_Party_id_Party INT,
    selvagem BOOLEAN DEFAULT true
);

/* Tabela para indicar se o Pokémon é Shiny */
CREATE TABLE Shiny (
    fk_Pokemon_Id_pokemon INT PRIMARY KEY,
    is_shiny BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (fk_Pokemon_Id_pokemon) REFERENCES Pokemon(Id_pokemon) ON DELETE CASCADE
);

/* Tabela de Treinadores */
CREATE TABLE Treinador (
    ID_treinador INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(50) NOT NULL,
    data_nasc DATE NOT NULL,
    genero VARCHAR(20) NOT NULL
);

/* Tabela de Documentos (normalizando o campo CPF) */
CREATE TABLE Documentos (
    id_documento INT PRIMARY KEY AUTO_INCREMENT,
    fk_Treinador_ID_treinador INT,
    tipo_documento VARCHAR(20) NOT NULL,
    numero_documento VARCHAR(20) NOT NULL,
    UNIQUE (tipo_documento, numero_documento),
    FOREIGN KEY (fk_Treinador_ID_treinador) REFERENCES Treinador(ID_treinador) ON DELETE CASCADE
);

/* Tabela de Movimentos */
CREATE TABLE movimentos (
    Id_Movimento INT PRIMARY KEY,
    dano INT,
    chanceDeAcerto FLOAT
);

/* Tabela de Party */
CREATE TABLE Party (
    id_Party INT PRIMARY KEY AUTO_INCREMENT,
    fk_Treinador_ID_treinador INT
);

/* Tabela de Elemento */
CREATE TABLE Elemento (
    id_elemento INT PRIMARY KEY,
    Nome VARCHAR(20)
);

/* Tabela Relacional Pokémon - Região */
CREATE TABLE poke_regiao (
    fk_Regiao_ID_regial INT NOT NULL,
    fk_Pokemon_Id_pokemon INT NOT NULL,
    PRIMARY KEY (fk_Regiao_ID_regial, fk_Pokemon_Id_pokemon)
);

/* Tabela Relacional Pokémon - Movimentos */
CREATE TABLE poke_mov (
    fk_Pokemon_Id_pokemon INT NOT NULL,
    fk_movimentos_Id_Movimento INT NOT NULL,
    PRIMARY KEY (fk_movimentos_Id_Movimento, fk_Pokemon_Id_pokemon)
);

/* Tabela Relacional Pokémon - Elemento */
CREATE TABLE Poke_elemento (
    fk_Pokemon_Id_pokemon INT NOT NULL,
    fk_Elemento_id_elemento INT NOT NULL,
    PRIMARY KEY (fk_Pokemon_Id_pokemon, fk_Elemento_id_elemento)
);

/* Chaves Estrangeiras e Restrições */

/* Party -> Pokemon */
ALTER TABLE Pokemon ADD CONSTRAINT FK_Pokemon_2
    FOREIGN KEY (fk_Party_id_Party)
    REFERENCES Party (id_Party)
    ON DELETE RESTRICT;

/* Treinador -> Party */
ALTER TABLE Party ADD CONSTRAINT FK_Party_2
    FOREIGN KEY (fk_Treinador_ID_treinador)
    REFERENCES Treinador (ID_treinador)
    ON DELETE CASCADE;

/* Região -> Poke_Região */
ALTER TABLE poke_regiao ADD CONSTRAINT FK_poke_regiao_1
    FOREIGN KEY (fk_Regiao_ID_regial)
    REFERENCES Regiao (ID_regial)
    ON DELETE RESTRICT;

/* Pokémon -> Poke_Região */
ALTER TABLE poke_regiao ADD CONSTRAINT FK_poke_regiao_2
    FOREIGN KEY (fk_Pokemon_Id_pokemon)
    REFERENCES Pokemon (Id_pokemon)
    ON DELETE RESTRICT;

/* Pokémon -> Poke_Mov */
ALTER TABLE poke_mov ADD CONSTRAINT FK_poke_mov_1
    FOREIGN KEY (fk_Pokemon_Id_pokemon)
    REFERENCES Pokemon (Id_pokemon)
    ON DELETE RESTRICT;

/* Movimentos -> Poke_Mov */
ALTER TABLE poke_mov ADD CONSTRAINT FK_poke_mov_2
    FOREIGN KEY (fk_movimentos_Id_Movimento)
    REFERENCES movimentos (Id_Movimento)
    ON DELETE RESTRICT;

/* Pokémon -> Poke_Elemento */
ALTER TABLE Poke_elemento ADD CONSTRAINT FK_Poke_elemento_1
    FOREIGN KEY (fk_Pokemon_Id_pokemon)
    REFERENCES Pokemon (Id_pokemon)
    ON DELETE RESTRICT;

/* Elemento -> Poke_Elemento */
ALTER TABLE Poke_elemento ADD CONSTRAINT FK_Poke_elemento_3
    FOREIGN KEY (fk_Elemento_id_elemento)
    REFERENCES Elemento (id_elemento);

/* Triggers */

/* Trigger para criar uma Party quando um Treinador é criado */
DELIMITER $$
CREATE TRIGGER criar_party 
AFTER INSERT ON Treinador 
FOR EACH ROW
BEGIN 
    INSERT INTO party(fk_Treinador_ID_treinador) VALUES(NEW.ID_treinador);
END$$
DELIMITER ;

/* Trigger para liberar Pokémon ao excluir uma Party */
DELIMITER $$
CREATE TRIGGER libertar_pokemon 
AFTER DELETE ON Party
FOR EACH ROW
BEGIN
    UPDATE Pokemon 
    SET selvagem = true
    WHERE fk_Party_id_Party = OLD.id_Party;
END$$
DELIMITER ;
