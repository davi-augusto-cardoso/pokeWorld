botao = document.getElementById("burger-bar");
menu = document.getElementById("menu");
conteudo = document.getElementById("conteudo");
descricao = document.getElementById("descricao");
mostrarPokemons();

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

function criarPokemon() {
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
    mostrarPokemons()

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
function getTreinadores(cols){
    fetch('treinador?cols=' + cols.join(','))  // Adicionado return
    .then(response => response.json())  // Converte a resposta para JSON
    .then(data => {
        console.log('treinadores encontrados:', data);  // Exibe os pokémons encontrados
        return data;  // Retorna os dados para uso posterior
    })
    .catch(error => {
        console.error('Erro:', error);
        return [];  // Retorna array vazio em caso de erro
    });
}

function getParty(fkparty){
    fetch(`pokemon/`)

}

let dictpokes = [];
async function mostrarPokemons() {

    dictpokes = JSON.parse(await getPokemons(["Id_pokemon","nome", "forca", "resistencia", "velocidade", "peso", "shyne", "nivel", "fk_party_id_Party"]));
    if(dictpokes < 0){
        console.log("Nenhum pokemon encontrado");
        return;
    }
    const card = document.getElementById("pokemons");
    card.innerHTML = ""
        dictpokes.forEach((pokemon) => {
            console.log(pokemon.nome);
            card.innerHTML += `<div class="pokemon" data-id=${pokemon['Id_pokemon']} onclick="mostrarDescricao(${pokemon["Id_pokemon"]})"> <h1> ${pokemon["nome"]}</h1> <button class=Botaodeletar onclick=botaoDeletar(${pokemon["Id_pokemon"]})><img src="pages/src/trash-blank-svgrepo-com.svg" alt="deletar" id="imgDeletar"></button> </div>`
})
}

let listTreinadores = [];
async function mostraTreinadores(){
     listTreinadores = JSON.parse(getTreinadores(['nome, idade, experiencia, ID_treinador']));
    if(listTreinadores < 0){
        console.log("Nenhum treinador encontrado");
        return;
    }
    const card = document.getElementById("pokemons");
    card.innerHTML = ""
    listTreinadores.forEach((treinador) => {
        card.innerHTML += `<div class="pokemon" data-id=${treinador['ID_treinador']} onclick="mostrarDescricaoTreinador(${treinador["ID_treinador"]})"> <h1> ${treinador["nome"]}</h1> <button class=Botaodeletar onclick=botaoDeletarTreinador(${treinador["ID_treinador"]})><img src="pages/src/trash-blank-svgrepo-com.svg" alt="deletar" id="imgDeletar"></button> </div>`})
}

function obterParty(ID_treinador){
    let parts = []
    for(pokes in dictpokes){
        if(pokes["fk_party_id_Party"] == ID_treinador){
            parts.push(pokes)
        }
    return parts
}
}

function mostraPokemonsParty(id){
    let party = obterParty(id)
    const card = document.getElementById("pokemons");
    card.innerHTML = ""
    party.forEach((pokemon) => {
        card.innerHTML += `<div class="pokemon" data-id=${pokemon['Id_pokemon']} onclick="mostrarDescricao(${pokemon["Id_pokemon"]})"> <h1> ${pokemon["nome"]}</h1> <button class=Botaodeletar onclick=botaoDeletar(${pokemon["Id_pokemon"]})><img src="pages/src/trash-blank-svgrepo-com.svg" alt="deletar" id="imgDeletar"></button> </div>`
    })
}

function mostrarDescricaoTreinador(ID_treinador) {
    let treinador;
    listTreinadores.forEach((treinador) => {
        if(treinador["ID_treinador"] == ID_treinador) {
            treinador = treinador;
        }
    })
    document.getElementById("discNome").value = treinador["nome"];
    document.getElementById("discIdade").value = treinador["idade"];
    document.getElementById("discExperiencia").value = treinador["experiencia"];
    document.getElementById("editar").dataset.id = ID_treinador;

    mostraPokemonsParty(ID_treinador)
}



// Chama a função para exibir os pokémons


function mostrarDescricao(id_pokemon) {
    let pkemon;
    
    dictpokes.forEach((pokemon) => {
    if(pokemon["Id_pokemon"] == id_pokemon) {
            pkemon = pokemon;
    }
    
    })

    document.getElementById("discNome").value = pkemon["nome"];
    document.getElementById("discforca").value = pkemon["forca"];
    document.getElementById("discresistencia").value = pkemon["resistencia"];
    document.getElementById("discvelocidade").value = pkemon["velocidade"];
    document.getElementById("discpeso").value = pkemon["peso"];
    document.getElementById("discshyne").value = pkemon["shyne"];
    document.getElementById("discnivel").value = pkemon["nivel"];
    document.getElementById("editar").dataset.id = id_pokemon;
}

function botaoDeletar(id){
    console.log(id)
    fetch(`pokemon/${id}`, {
        method: 'DELETE',
    })
}

function mostraModal(){
    if (document.getElementById("fundoModal").style.display == "none") {
        document.getElementById("fundoModal").style.display = "flex";
    } else {
        document.getElementById("fundoModal").style.display = "none";
    }
}




function editarPokemon(){
    nome = document.getElementById("discNome").value;
    forca = document.getElementById("discforca").value;
    resistencia = document.getElementById("discresistencia").value;
    velocidade = document.getElementById("discvelocidade").value;
    peso = document.getElementById("discpeso").value;
    shyne = document.getElementById("discshyne").value;
    nivel = document.getElementById("discnivel").value;
    id = document.getElementById("editar").dataset.id;
    
    fetch(`pokemon/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nome: nome, forca: forca, resistencia: resistencia, velocidade: velocidade, peso: peso, shyne: shyne, nivel: nivel})
    })
}



const abaPokemon = document.getElementById("abaPokemon")
const abaTreinador = document.getElementById("abaTreinador")
abaPokemon.addEventListener("click", mostrarPokemons)

function criaTreinador(){
    let values = {nome: "", idade: 0, experiencia: 0};
    if (document.getElementById("nome").value == "" || document.getElementById("idade").value == "" || document.getElementById("experiencia").value == "") {
        alert("Favor preencher todos os campos");
        return;
    } else {
        values.nome = document.getElementById("nome").value;
        values.idade = parseInt(document.getElementById("idade").value);
        values.experiencia = parseInt(document.getElementById("experiencia").value);
    }
    // console.log(values);
    let json =JSON.stringify(values)
    
    fetch('treinador', {
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
    mostraTreinadores()
}