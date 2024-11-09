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

async function getPokemons(cols) {
    return fetch('pokemon?cols=' + cols.join(','))  
        .then(response => response.json())  
        .then(data => {
            console.log('Pokémons encontrados:', data);
            return data;
        })
        .catch(error => {
            console.error('Erro:', error);
            return [];
        });
}

async function getTreinadores(cols){
    return fetch('treinador?cols=' + cols.join(','))  
        .then(response => response.json())  
        .then(data => {
            console.log('Treinadores encontrados:', data); 
            return data;
        })
        .catch(error => {
            console.error('Erro:', error);
            return [];
        });
}
function getParty(idTreinador){
    fetch(`party/${idTreinador}`)
    .then(resp => resp.json())
    .then(data => {
        return data;
    }) // Adicionado return
}

let dictpokes = [];
async function mostrarPokemons() {
    let botaoAdicionar = document.getElementById("adicionar");
    botaoAdicionar.onclick = mostraModalpoke;
    dictpokes = JSON.parse(await getPokemons(["Id_pokemon", "nome", "forca", "resistencia", "velocidade", "peso", "shyne", "nivel", "fk_party_id_Party"]));
    
    if (dictpokes.length === 0) {
        console.log("Nenhum Pokémon encontrado");
        return;
    }

    const card = document.getElementById("pokemons");
    card.innerHTML = "";  // Limpa o conteúdo atual
    dictpokes.forEach((pokemon) => {
        console.log(pokemon.nome);
        card.innerHTML += `<div class="pokemon" data-id=${pokemon['Id_pokemon']} onclick="mostrarDescricaoPokemon(${pokemon["Id_pokemon"]})">
                              <h1>${pokemon["nome"]}</h1>
                              <button class="Botaodeletar" onclick="botaoDeletar(${pokemon["Id_pokemon"]})">
                                  <img src="pages/src/trash-blank-svgrepo-com.svg" alt="deletar" id="imgDeletar">
                              </button>
                           </div>`;
    });
}

let listTreinadores = [];
    
async function mostraTreinadores() {
    botaoAdicionar = document.getElementById("adicionar").onclick = mostraModaltreinador;
    listTreinadores = JSON.parse(await getTreinadores(["ID_treinador","nome",]));
    
    if (listTreinadores.length == 0) {
        console.log("Nenhum treinador encontrado");
        return;
    }

    const card = document.getElementById("pokemons");
    card.innerHTML = "";
    listTreinadores.forEach((treinador) => {
        card.innerHTML += `<div class="pokemon" data-id=${treinador['ID_treinador']} onclick="mostrarDescricaoTreinador(${treinador["ID_treinador"]})">
                               <h1>${treinador["nome"]}</h1>
                               <button class="Botaodeletar" onclick="botaoDeletarTreinador(${treinador["ID_treinador"]})">
                                   <img src="pages/src/trash-blank-svgrepo-com.svg" alt="deletar" id="imgDeletar">
                               </button>
                           </div>`;
    });
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


function mostrarDescricaoPokemon(id_pokemon) {
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

function mostraModalpoke(){
    if (document.getElementById("fundoModalpoke").style.display == "none") {
        document.getElementById("fundoModalpoke").style.display = "flex";
    } else {
        document.getElementById("fundoModalpoke").style.display = "none";
    }
}

function mostraModaltreinador(){
    if (document.getElementById("fundoModaltreiner").style.display == "none") {
        document.getElementById("fundoModaltreiner").style.display = "flex";
    } else {
        document.getElementById("fundoModaltreiner").style.display = "none";
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

function criaTreinador(){
    let values = {nome: "", idade: 0,data_nasc:"", genero:"",cpf:""};

        values.nome = document.getElementById("nomeTreinador").value;
        values.data_nasc = document.getElementById("data_nascTreinador").value;
        values.cpf = document.getElementById("cpfTreinador").value;
        values.genero = document.getElementById("generoTreinador").value;

    let json =JSON.stringify(values)
    
    fetch('treinador', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: json // Converte o objeto para uma string JSON
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