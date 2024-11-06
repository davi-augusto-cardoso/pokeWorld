from imports import json, os, mysql

class CRUD:
    
    def __init__(self) -> None:
        self.__cursor = None
        self.__connection = None
    
    def open_connection(self) -> int:
        """Abre uma conexao com o banco de dados e cria um cursor para realizar queries."""
        credentials = self.__get_credentials()
        
        try:
            # Configurações de conexão
            self.__connection = mysql.connect(**credentials)
            
            # Cria um cursor para interagir com o banco de dados
            self.__cursor = self.__connection.cursor()
            print("Conexão estabelecida com sucesso!")
            return 1
        except mysql.OperationalError as error:
            print(f"Erro de conexao: {error}")
            return -1
    
    def close_connection(self) -> int:
        """Encerra a conexao com o banco de dados fechando o cursor e a conexao."""
        try:
            if self.__cursor:
                self.__cursor.close()
                
            if self.__connection:
                self.__connection.close()
                print("Conexao encerrada.")
                return 1
                
        except mysql.Error as error:
            print(f"Erro ao encerrar a conexao: {error}")
            return -1
    
    def create(self, table: str, name_values:list, values: list) -> int:
        """Insere um novo registro na tabela especificada."""
        query = f"INSERT INTO {table} ({', '.join(name_values)}) VALUES ({', '.join(['%s'] * len(values))})"

        try:
            self.__cursor.execute(query, tuple(values))
            self.__connection.commit()
            print("Insercao realizada com sucesso.")
            return 1
            
        except mysql.DatabaseError as error:
            print(f"Erro de banco de dados: {error}")
            return -1
    
    def read(self, table: str, cols: tuple, where_conditions: dict = None):
        """Realiza uma consulta SELECT nas colunas especificadas de uma tabela com condições opcionais e retorna os dados em formato JSON."""
        query = f"SELECT {', '.join(cols)} FROM {table}"
        
        if where_conditions:
            where_clause = ' AND '.join([f"{col} = %s" for col in where_conditions])
            query += " WHERE " + where_clause

        try:
            self.__cursor.execute(query, tuple(where_conditions.values()) if where_conditions else None)
            result = self.__cursor.fetchall()

            # Converte os resultados para uma lista de dicionários (um por linha de dados)
            columns = [desc[0] for desc in self.__cursor.description]  # Obtém os nomes das colunas
            result_dict = [dict(zip(columns, row)) for row in result]  # Junta as colunas com os dados

            # Retorna os dados como JSON
            json_result = json.dumps(result_dict, ensure_ascii=False)

            print("Leitura realizada com sucesso.")
            return json_result
            
        except mysql.Error as error:
            print(f"Erro de operação: {error}")
            return -1
    
    def update(self, table: str, set_values: dict, id_key: str, id_value: int) -> int:
        """Atualiza registros em uma tabela com base nas condicoes fornecidas."""
        
        # Garantir que os valores de tipo string sejam colocados entre aspas
        set_clause = ', '.join([f"{col} = %s" for col in set_values.keys()])
        
        query = f"UPDATE {table} SET {set_clause} WHERE {id_key} = %s"

        # Prepare os valores a serem passados para a query, incluindo o valor do ID
        values = list(set_values.values()) + [id_value]

        try:
            self.__cursor.execute(query, values)  # Passa os valores de forma segura
            self.__connection.commit()
            print("Atualizacao realizada com sucesso.")
            return 1
            
        except mysql.Error as error:
            print(f"Erro de operacao: {error}")
            return -1

    def delete(self, table: str, id_key:str,  id_value:int) -> int:
        """Remove registros de uma tabela com base nas condicoes fornecidas."""
        query = f"DELETE FROM {table} WHERE {id_key} = {id_value}"
        try:
            self.__cursor.execute(query)
            self.__connection.commit()
            print("Exclusao realizada com sucesso.")
            return 1
            
        except mysql.Error as error:
            print(f"Erro de operacao: {error}")
            return -1
        
    def __get_credentials(self):
        file_path = 'credentials.json'
        credentials = None

        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    credentials = json.load(file)
            except UnicodeDecodeError:
                print("Erro de encoding ao ler o arquivo JSON. Verifique o encoding ou corrija o arquivo.")
                raise
            except json.JSONDecodeError:
                print("Arquivo JSON está corrompido ou contém dados inválidos.")
                raise
        else:
            credentials = {
                'host':     input("Digite o host: "),
                'port':     input("Digite a porta:"),
                'user':     input("Digite o usuário: "),
                'password': input("Digite a senha: "),
                'database': input("Digite o nome do database: ")
            }
            
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(credentials, file, ensure_ascii=False)

        return credentials
