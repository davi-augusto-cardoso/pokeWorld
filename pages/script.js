botao = document.getElementById("burger-bar");
menu = document.getElementById("menu");
conteudo = document.getElementById("conteudo");
descricao = document.getElementById("descricao");

function mostraMenu() {
    if (menu.style.display === "none") {
        document.getElementById("burger-bar").innerHTML = "<img src='src/burger-menu-right-svgrepo-com.svg' alt='Botão de menu'></img>";
        conteudo.style.width = "60vw";
        descricao.style.width = "18vw";
        menu.style.display = "flex";
    } else {
        document.getElementById("burger-bar").innerHTML = "<img src='src/burger-menu-svgrepo-com.svg' alt='Botão de menu'></img>";
        conteudo.style.width = "73vw";
        descricao.style.width = "25vw";
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
    
    fetch('pokemon', {
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
    return fetch('pokemon?cols=' + cols.join(','))  // Adicionado return
        .then(response => response.json())  // Converte a resposta para JSON
        .then(data => {
            console.log('Pokémons encontrados:', data);  // Exibe os pokémons encontrados
            return data;  // Retorna os dados para uso posterior
        })
        .catch(error => {
            console.error('Erro:', error);
            return [];  // Retorna array vazio em caso de erro
        });
}
let dictpokes = [];
async function mostrarPokemons() {
    dictpokes = JSON.parse(await getPokemons(["Id_pokemon","nome", "forca", "resistencia", "velocidade", "peso", "shyne", "nivel"]));
    if(dictpokes < 0){
        console.log("Nenhum pokemon encontrado");
        return;
    }
    console.log(typeof( dictpokes));
    const card = document.getElementById("pokemons");
        dictpokes.forEach((pokemon) => {
            console.log(pokemon.nome);
            card.innerHTML += '<div class="pokemon" id= "pokemon" data-id="'+ pokemon["Id_pokemon"] +'" onclick="mostrarDescricao('+pokemon["Id_pokemon"]+')"> <h1>' + pokemon["nome"] + '</h1> <button id="deletar"> <img src="src/trash-blank-svgrepo-com.svg" alt="deletar" id="imgDeletar"></button> </div>';
        });
    console.log("Lista pokes"+dictpokes);
}

// Chama a função para exibir os pokémons
mostrarPokemons();

function mostrarDescricao(id_pokemon) {
    document.getElementById("descricao").style.display
    dictpokes.forEach((pokemon) => {
    if (pokemon["Id_pokemon"] == id_pokemon) {
            document.get
        }
    })
}

