from imports import pcg, sql

class CRUD:
    
    def __init__(self) -> None:
        self.__cursor       = None
        self.__connection   = None
    
    def open_connection(self, host:str, database:str, user:str, password:str)->int:
        """
        Abre uma conexão com o banco de dados e cria um cursor para realizar querys.
        Args:
            host (str): O nome do host em que deseja se conectar
            database (str): O nome do database em que deseja se conectar
            user (str): O user do database que deseja se conectar
            password (str): A senha do user que deseja se conectar
        Returns:
            1 -> Sucesso | -1 -> Falha
        """
        try:
            # Configurações de conexão
            self.__connection = pcg.connect(host, database, user, password)
            
            # Cria um cursor para interagir com o banco de dados
            self.__cursor = self.__connection.cursor()
        except pcg.OperationalError as error:
            print(f"\033[91m{error}\033[0m")
    
    def close_connection(self)->int:
        """Encerra conexão com o banco de dados fechando o cursor e a conexão.
        Returns:
            1 -> Sucesso | -1 -> Falha
        """
        try:
            if self.__cursor:
                self.__cursor.close()
                
            if self.__connection:
                self.__connection.close()
                print("\033[34m Conexão encerrada.\033[0m")
                return 1
                
        except pcg.OperationalError as error:
            print(f"\033{error}\033[0m")
            return -1
    
    def create(self, table: str, values: tuple) -> int:
        """
        Insere um novo registro na tabela especificada.

        :param table: Nome da tabela
        :param values: Tupla com os valores a serem inseridos
        :return: 1 se a inserção foi bem-sucedida, -1 em caso de erro
        """
        # Cria uma consulta SQL segura para inserção
        query = sql.SQL("INSERT INTO {table} VALUES ({values})").format(
            table=sql.Identifier(table),
            values=sql.SQL(', ').join(sql.Placeholder() * len(values))  # Cria placeholders
        )
        
        try:
            # Executa a consulta com os valores fornecidos
            self.__cursor.execute(query, values)
            self.__connection.commit()
            print("\033[34mInserção realizada com sucesso.\033[0m")
            return 1
            
        except pcg.DatabaseError as error:
            print(f"\033[31mErro de banco de dados: {error}\033[0m")
            return -1
    
    def read(self, table: str, cols: tuple, where_conditions: dict = None):
        """
        Realiza uma consulta SELECT nas colunas especificadas de uma tabela com condições opcionais.
        
        :param table: Nome da tabela
        :param cols: Tupla contendo os nomes das colunas a serem lidas
        :param conditions: Dicionário com condições para o WHERE {coluna: valor}
        :return: Dados lidos ou -1 em caso de erro
        """
        # Cria a consulta SQL para leitura
        query = sql.SQL("SELECT {values} FROM {table}").format(
            table=sql.Identifier(table),
            values=sql.SQL(', ').join(sql.Identifier(col) for col in cols)
        )
        
        # Adiciona a cláusula WHERE, se houver condições
        if where_conditions:
            where_clause = sql.SQL(' AND ').join(
                sql.Composed([sql.Identifier(col), sql.SQL(" = "), sql.Placeholder(col)]) for col in conditions
            )
            query = query + sql.SQL(" WHERE ") + where_clause

        try:
            # Executa a consulta com as condições, se houver
            self.__cursor.execute(query, where_conditions)
            result = self.__cursor.fetchall()
            print("\033[34mLeitura realizada com sucesso.\033[0m")
            return result
            
        except pcg.OperationalError as error:
            print(f"\033[31mErro de operação: {error}\033[0m")
            return -1
    
    def update(self, table: str, set_values: dict, where_conditions: dict = None) -> int:
        """
        Atualiza registros em uma tabela com base nas condições fornecidas.

        :param table: Nome da tabela
        :param set_values: Dicionário contendo os valores a serem atualizados {coluna: valor}
        :param where_conditions: Dicionário contendo as condições de atualização {coluna: valor}
        :return: 1 se a atualização foi bem-sucedida, -1 se houve um erro
        """
        # Construção da consulta SQL dinâmica
        query = sql.SQL("UPDATE {table} SET {set_clause} WHERE {where_clause}").format(
            table=sql.Identifier(table),
            set_clause=sql.SQL(', ').join(
                sql.Composed([sql.Identifier(col), sql.SQL(" = "), sql.Placeholder(col)]) for col in set_values
            ),
            where_clause=sql.SQL(' AND ').join(
                sql.Composed([sql.Identifier(col), sql.SQL(" = "), sql.Placeholder(col)]) for col in where_conditions
            )
        )

        # Combina os valores para o SET e WHERE
        values = {**set_values, **where_conditions}

        try:
            # Executa a consulta com os valores fornecidos
            self.__cursor.execute(query, values)
            self.__connection.commit()
            print("\033[34m Atualização realizada com sucesso.\033[0m")
            return 1
            
        except pcg.OperationalError as error:
            print(f"\033[31mErro de operação: {error}\033[0m")
            return -1
    
    def delete(self, table: str, where_conditions: dict= None) -> int:
        """
        Remove registros de uma tabela com base nas condições fornecidas.

        :param table: Nome da tabela
        :param conditions: Dicionário com condições para o WHERE {coluna: valor}
        :return: 1 se a exclusão foi bem-sucedida, -1 em caso de erro
        """
        # Cria a consulta SQL para exclusão
        query = sql.SQL("DELETE FROM {table}").format(
            table=sql.Identifier(table)
        )
        
        # Adiciona a cláusula WHERE, se houver condições
        if where_conditions:
            where_clause = sql.SQL(' AND ').join(
                sql.Composed([sql.Identifier(col), sql.SQL(" = "), sql.Placeholder(col)]) for col in conditions
            )
            query = query + sql.SQL(" WHERE ") + where_clause
        else:
            print("\033[31mErro: Condições de exclusão não fornecidas.\033[0m")
            return -1

        try:
            # Executa a consulta com as condições fornecidas
            self.__cursor.execute(query, where_conditions)
            self.__connection.commit()
            print("\033[34mExclusão realizada com sucesso.\033[0m")
            return 1
            
        except pcg.OperationalError as error:
            print(f"\033[31mErro de operação: {error}\033[0m")
            return -1
        