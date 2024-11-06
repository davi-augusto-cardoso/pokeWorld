botao = document.getElementById("burger-bar");
menu = document.getElementById("menu");

function mostraMenu() {
    if (menu.style.display === "none") {
        document.getElementById("burger-bar").innerHTML = "<img src='src/burger-menu-right-svgrepo-com.svg' alt='Botão de menu'></img>";
        menu.style.display = "flex";
    } else {
        document.getElementById("burger-bar").innerHTML = "<img src='src/burger-menu-svgrepo-com.svg' alt='Botão de menu'></img>";
        menu.style.display = "none";
    }

}

function criarJson() {
    let values = {nome: "", forca: 0, resistencia: 0, velocidade: 0, peso: 0, shyne: false, nivel: 0};
    if (document.getElementById("nome").value == "" || document.getElementById("forca").value == "" || document.getElementById("resistencia").value == "" || document.getElementById("velocidade").value == "" || document.getElementById("peso").value == "" || document.getElementById("nivel").value == "") {
        alert("Favor preencher todos os campos");
        return;
    } else {
        values.nome = document.getElementById("nome").value;
        values.forca = parseInt(document.getElementById("forca").value);
        values.resistencia = parseInt(document.getElementById("resistencia").value);
        values.velocidade = parseInt(document.getElementById("velocidade").value);
        values.peso = parseFloat(document.getElementById("peso").value);
        if (document.getElementById("shyne").checked) {
            values.shyne = true;
        } else {
            values.shyne = false;
        }
        values.nivel = parseInt(document.getElementById("nivel").value);
    }
    // console.log(values);
    let json =JSON.stringify(values)
    
    fetch('http://127.0.0.1:5000/add_pokemon', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(values) // Converte o objeto para uma string JSON
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao enviar dados');
        }
        return response.json(); // Obtém a resposta JSON (opcional)
    })
    .then(data => {
        console.log('Resposta do servidor:', data); // Manipula a resposta
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function getPokemons(cols) {
    fetch('http://127.0.0.1:5000/list_pokemons')
        .then(response => response.json())  // Converte a resposta para JSON
        .then(data => {
            if (data.error) {
                console.log(data.error);  // Exibe erro se não encontrar pokémons
            } else {
                console.log(data);  // Exibe os pokémons retornados
            }
        })
        .catch(error => console.error('Erro na requisição:', error));  // Caso ocorra algum erro
}

// Exemplo de chamada passando as colunas
getPokemons(['nome', 'forca', 'peso']);


// http://127.0.0.1:5000
// @app.route('/add_pokemon', methods=['POST'])