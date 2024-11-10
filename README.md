# PokeWorld 🚀

> Um catalogo do mundo pokemon.

## Pré-requisitos 📋

Certifique-se de ter o **Python 3.8** ou superior instalado em sua máquina.

## Instalação ⚙️

### 1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/nome_do_projeto.git
cd nome_do_projeto
```

### 2. Instale as dependências

Para instalar as dependências globalmente, execute:

```bash
python install_requiriments.py
```

> **Nota:** Esse comando instala as bibliotecas listadas em `requirements.txt`. Verifique se você possui permissões de administrador (ou use `sudo`, se necessário).

## Estrutura dos Arquivos 📁

Este projeto é composto pelos seguintes arquivos principais:

- **crud.py**: Contém a classe `CRUD` para realizar operações de banco de dados, incluindo inserção, leitura, atualização e exclusão. Utiliza o módulo `psycopg2` para conexão e execução de comandos SQL.
  - **Métodos principais**:
    - `open_connection()`: Abre uma conexão com o banco de dados.
    - `close_connection()`: Fecha a conexão com o banco de dados.
    - `create()`: Insere dados em uma tabela especificada.
    - `read()`: Lê dados de uma tabela com condições opcionais.
    - `update()`: Atualiza registros em uma tabela com base em condições.
    - `delete()`: Remove registros de uma tabela com base em condições.

- **install_requiriments.py**: Script para instalar todas as dependências listadas em `requirements.txt`. Este script verifica a instalação do Python e executa o comando para instalar pacotes globalmente.

- **poke_api.py**: Executa a aplicação principal e usa a classe `CRUD` para realizar operações. Este arquivo também configura a API utilizando Flask, possibilitando endpoints para a aplicação.

## Como Usar 🛠️

1. Certifique-se de que as informações de conexão com o banco de dados estão configuradas corretamente no arquivo `crud.py`.
2. Execute o arquivo `poke_api.py` para iniciar a aplicação:
   ```bash
   python poke_api.py
   ```
3. A aplicação estará pronta para receber requisições via API.

## Exemplo de Uso 💻

Abaixo está um exemplo de como usar a classe `CRUD` no seu código:

```python
from crud import CRUD

crud = CRUD()
crud.open_connection("localhost", "meu_banco", "meu_usuario", "minha_senha")

# Exemplo de inserção
resultado = crud.create("tabela_exemplo", ("valor1", "valor2"))
print("Resultado da inserção:", resultado)

# Exemplo de leitura
dados = crud.read("tabela_exemplo", ("coluna1", "coluna2"))
print("Dados lidos:", dados)

crud.close_connection()
```

## Licença 📜

Este projeto está licenciado sob a [Kiba não Pray] - consulte o arquivo LICENSE para obter detalhes.

---

**Nota:** Substitua `"localhost"`, `"meu_banco"`, `"meu_usuario"`, e `"minha_senha"` pelas configurações do seu banco de dados.

versao pronta