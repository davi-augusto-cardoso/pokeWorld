from imports import json, os, mysql

class CRUD:
    
    def __init__(self) -> None:
        self.__cursor = None
        self.__connection = None
    
    def open_connection(self) -> int:
        """Abre uma conexão com o banco de dados e cria um cursor para realizar queries."""
        credentials = self.__get_credentials()
        
        try:
            # Configurações de conexão
            self.__connection = mysql.connect(**credentials)
            
            # Cria um cursor para interagir com o banco de dados
            self.__cursor = self.__connection.cursor()
            print("Conexão estabelecida com sucesso!")
            return 1
        except mysql.OperationalError as error:
            print(f"Erro de conexão: {error}")
            return -1
    
    def close_connection(self) -> int:
        """Encerra a conexão com o banco de dados fechando o cursor e a conexão."""
        try:
            if self.__cursor:
                self.__cursor.close()
                
            if self.__connection:
                self.__connection.close()
                print("Conexão encerrada.")
                return 1
                
        except mysql.Error as error:
            print(f"Erro ao encerrar a conexão: {error}")
            return -1
    
    def create(self, table: str, name_values:list, values: list) -> int:
        """Insere um novo registro na tabela especificada."""
        query = f"INSERT INTO {table} ({', '.join(name_values)}) VALUES ({', '.join(['%s'] * len(values))})"

        try:
            self.__cursor.execute(query, tuple(values))
            self.__connection.commit()
            print("Inserção realizada com sucesso.")
            return 1
            
        except mysql.DatabaseError as error:
            print(f"Erro de banco de dados: {error}")
            return -1
    
    def read(self, table: str, cols: tuple, where_conditions: dict = None):
        """Realiza uma consulta SELECT nas colunas especificadas de uma tabela com condições opcionais."""
        query = f"SELECT {', '.join(cols)} FROM {table}"
        
        if where_conditions:
            where_clause = ' AND '.join([f"{col} = %s" for col in where_conditions])
            query += " WHERE " + where_clause

        try:
            self.__cursor.execute(query, tuple(where_conditions.values()) if where_conditions else None)
            result = self.__cursor.fetchall()
            print("Leitura realizada com sucesso.")
            return result
            
        except mysql.Error as error:
            print(f"Erro de operação: {error}")
            return -1
    
    def update(self, table: str, set_values: dict, where_conditions: dict = None) -> int:
        """Atualiza registros em uma tabela com base nas condições fornecidas."""
        set_clause = ', '.join([f"{col} = %s" for col in set_values])
        where_clause = ' AND '.join([f"{col} = %s" for col in where_conditions]) if where_conditions else ""

        query = f"UPDATE {table} SET {set_clause}"
        if where_conditions:
            query += " WHERE " + where_clause

        values = list(set_values.values()) + (list(where_conditions.values()) if where_conditions else [])
        
        try:
            self.__cursor.execute(query, values)
            self.__connection.commit()
            print("Atualização realizada com sucesso.")
            return 1
            
        except mysql.Error as error:
            print(f"Erro de operação: {error}")
            return -1
    
    def delete(self, table: str, where_conditions: dict = None) -> int:
        """Remove registros de uma tabela com base nas condições fornecidas."""
        query = f"DELETE FROM {table}"
        
        if where_conditions:
            where_clause = ' AND '.join([f"{col} = %s" for col in where_conditions])
            query += " WHERE " + where_clause
        else:
            print("Erro: Condições de exclusão não fornecidas.")
            return -1

        try:
            self.__cursor.execute(query, tuple(where_conditions.values()) if where_conditions else None)
            self.__connection.commit()
            print("Exclusão realizada com sucesso.")
            return 1
            
        except mysql.Error as error:
            print(f"Erro de operação: {error}")
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
