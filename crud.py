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
            self.__connection = pcg.connect(
                host="localhost",
                database="seu_banco",
                user="seu_usuario",
                password="sua_senha"
            )
            
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
    
    def create(self, table:str, values:tuple)->int:
        # Cria uma consulta SQL segura para inserção
        query = sql.SQL("INSERT INTO {table} VALUES ({values})").format(
            table=sql.Identifier(table),
            values=sql.SQL(', ').join(sql.Placeholder() * len(values))  # Cria placeholders
        )
        
        try:
            # Executa a consulta com os valores fornecidos
            self.__cursor.execute(query, values)
            self.__connection.commit()
            print("\033[34m Inser.\033[0m")
            return 1
            
        except pcg.OperationalError as error:
            print(f"\033{error}\033[0m")
            return -1
    
    def read(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass
        