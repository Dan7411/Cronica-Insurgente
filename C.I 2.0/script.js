// ==========================================
// CRÔNICA INSURGENTE - SCRIPT COMPLETO
// PARTE 1
// ==========================================


// ==========================================
// VARIÁVEIS GLOBAIS
// ==========================================

let partidaId = null;
let jogoAtivo = false;
let turno = "";

let velocidadeTexto = 25;

let evento70 = false;
let evento40 = false;
let evento15 = false;


// VIDA GLOBAL DO INIMIGO

let vidaInimigoMaxima = 170;
let vidaInimigoAtual = 170;


// VIDA GLOBAL DO JOGADOR

let vidaJogadorMaxima = 170;
let vidaJogadorAtual = 170;


// ==========================================
// PERSONAGENS
// ==========================================

const jogador = {

    nome: "Arauto da Rebelião",

    vidaMaxima: vidaJogadorMaxima,
    vida: vidaJogadorAtual,

    energiaMaxima:100,
    energia:0,

    pocoes:2,

    defesa:false,

    queimadura:0,
    sangramento:0,
    enfraquecido:0,

    criticoBonus:0,

    supremoUsado: false,
    energiaBloqueada: false

};



const inimigo = {

    nome:"Nêmesis Primordial",

    vidaMaxima: vidaInimigoMaxima,
    vida: vidaInimigoAtual,

    energiaMaxima:100,
    energia:0,

    pocoes:2,

    defesa:false,

    queimadura:0,
    sangramento:0,
    enfraquecido:0,

    criticoBonus:10,

    supremoUsado: false,
    energiaBloqueada: false

};




// ==========================================
// ATAQUES DO JOGADOR
// ==========================================


const ataquesJogador = {


ruina:{

    nome:"Ruína Celestial",
    dano:16,
    energia:15,
    efeito:"normal"

},


julgamento:{

    nome:"Julgamento da Rebelião",
    dano:14,
    energia:20,
    efeito:"queimadura"

},


destino:{

    nome:"Dilacerar o Destino",
    dano:10,
    energia:20,
    efeito:"duplo"

},


alvorecer:{

    nome:"Último Alvorecer",
    dano:30,
    energia:35,
    efeito:"erro"

},


supremo:{

    nome:"Aurora da Humanidade",
    dano:55,
    energia:100,
    efeito:"supremo"

}


};





// ==========================================
// ATAQUES DO INIMIGO
// ==========================================


const ataquesInimigo = {


colapso:{

    nome:"Colapso do Mundo",
    dano:18,
    energia:15,
    efeito:"normal"

},


eclipse:{

    nome:"Eclipse Absoluto",
    dano:11,
    energia:20,
    efeito:"duplo"

},


julgamento:{

    nome:"Julgamento Eterno",
    dano:14,
    energia:20,
    efeito:"enfraquecer"

},


aniquilacao:{

    nome:"Aniquilação Primordial",
    dano:30,
    energia:35,
    efeito:"erro"

},


supremo:{

    nome:"Fim da Criação",
    dano:60,
    energia:100,
    efeito:"supremo"

}


};





// ==========================================
// ELEMENTOS HTML
// ==========================================


let menu;
let historia;
let jogo;

let textoHistoria;
let mensagens;


let barraJogador;
let barraInimigo;


let energiaJogadorBarra;
let energiaInimigoBarra;


let vidaJogador;
let vidaInimigo;


let energiaJogador;
let energiaInimigo;


let pocoesJogador;
let pocoesInimigo;


let efeitosJogador;
let efeitosInimigo;


let textoTurno;




// ==========================================
// LIMPAR TERMINAL
// ==========================================


function limparMensagens(){

    if(mensagens){

        mensagens.innerHTML="";

    }

}

// ==========================================
// UTILIDADES
// ==========================================


function esperar(ms){

    return new Promise(resolve=>setTimeout(resolve,ms));

}



function irParaTopo(){

    window.scrollTo({

        top:0,
        behavior:"smooth"

    });

}






async function escrever(texto) {
    const linha = document.createElement("p");

    linha.textContent = "";
    mensagens.appendChild(linha);

    // Efeito de escrita
    for (let letra of texto) {
        linha.textContent += letra;
        await esperar(velocidadeTexto);
    }

    // Quando o quadro ficar cheio, mantém só as 4 últimas
    if (mensagens.scrollHeight > mensagens.clientHeight) {
        while (mensagens.children.length > 4) {
            mensagens.removeChild(mensagens.firstElementChild);
        }
    }

    // Posiciona o histórico
    mensagens.scrollTop = 0;
}






function esconderTelas(){

    menu.classList.add("escondido");

    historia.classList.add("escondido");

    jogo.classList.add("escondido");

}





// ==========================================
// ATUALIZAÇÃO DA INTERFACE
// ==========================================


function atualizarInterface(){


    barraJogador.style.width=
    (jogador.vida/jogador.vidaMaxima*100)+"%";


    barraInimigo.style.width=
    (inimigo.vida/inimigo.vidaMaxima*100)+"%";



    vidaJogador.innerHTML=
    "❤️ Vida: "+jogador.vida+" / "+jogador.vidaMaxima;



    vidaInimigo.innerHTML=
    "❤️ Vida: "+inimigo.vida+" / "+inimigo.vidaMaxima;




    energiaJogadorBarra.style.width=
    (jogador.energia/100*100)+"%";



    energiaInimigoBarra.style.width=
    (inimigo.energia/100*100)+"%";



    energiaJogador.innerHTML=
    "⚡ Energia: "+jogador.energia+"/100";


    energiaInimigo.innerHTML=
    "⚡ Energia: "+inimigo.energia+"/100";



    pocoesJogador.innerHTML=
    "🧪 Poções: "+jogador.pocoes;


    pocoesInimigo.innerHTML=
    "🧪 Poções: "+inimigo.pocoes;


}




// ==========================================
// CONTROLE DOS BOTÕES
// ==========================================


function ativarBotoes(){

    document.querySelectorAll(".acoes button")
    .forEach(botao=>{

        botao.disabled=false;

    });

}



function desativarBotoes(){

    document.querySelectorAll(".acoes button")
    .forEach(botao=>{

        botao.disabled=true;

    });

}




// ==========================================
// DANO
// ==========================================


function critico(atacante){

    let chance=20+atacante.criticoBonus;

    return Math.random()*100 < chance;

}




function calcularDano(atacante,alvo,dano){



    if(critico(atacante)){

        dano=Math.floor(dano*1.8);

        escrever("💥 ACERTO CRÍTICO!");

    }



    if(alvo.defesa){

        dano=Math.floor(dano/2);

        alvo.defesa=false;

        escrever("🛡 Defesa reduziu o dano!");

    }



    return dano;

}





function causarDano(alvo,dano){


    alvo.vida-=dano;


    if(alvo.vida<0)

        alvo.vida=0;


    atualizarInterface();


}





function ganharEnergia(personagem, quantidade) {
    if (personagem.energiaBloqueada) return;

    personagem.energia = Math.min(
        personagem.energia + quantidade,
        personagem.energiaMaxima
    );

    atualizarInterface();
}







// ==========================================
// ATAQUES DO JOGADOR
// ==========================================



async function usarAtaque(tipo){



if(!jogoAtivo || turno!="jogador")
return;



let ataque=ataquesJogador[tipo];


desativarBotoes();



await escrever(
"⚔ "+jogador.nome+
" usou "+ataque.nome
);





if(ataque.efeito=="duplo"){



for(let i=0;i<2;i++){


let dano=calcularDano(
jogador,
inimigo,
ataque.dano
);



causarDano(inimigo,dano);



await escrever(
"💥 Golpe "+(i+1)+": -"+dano+" HP"
);


await esperar(500);


}



}



else{


let dano=calcularDano(
jogador,
inimigo,
ataque.dano
);



causarDano(inimigo,dano);



await escrever(
"💥 -"+dano+" HP"
);



}





if (ataque.efeito == "queimadura") {

    inimigo.queimadura = 3;

    try {
        await enviarEfeito(
            inimigo,
            "queimadura",
            3
        );

        await escrever(
            "🔥 Nêmesis sofreu queimadura!"
        );

    } catch (erro) {
        console.error(
            "Erro ao registrar a queimadura:",
            erro
        );

        await escrever(
            "⚠ A queimadura foi aplicada, mas não foi possível registrá-la no banco."
        );
    }
}



  ganharEnergia(jogador, ataque.energia);

  
if (inimigo.vida <= 0) {
    try {
        await enviarStatusTurno("Ataque", jogador.nome);
    } catch (erro) {
        console.error(
            "Erro ao salvar o ataque final:",
            erro
        );
    }

    fimJogo();
    return;
}

await finalizarTurnoJogador("Ataque");

}



async function finalizarTurnoJogador(tipoAcao) {
  try {
    await enviarStatusTurno(tipoAcao, jogador.nome);
  } catch (erro) {
    console.error("Erro ao salvar o turno:", erro);
  }

  turno = "inimigo";
  textoTurno.innerHTML = "Turno: " + inimigo.nome;

  setTimeout(() => {
    turnoInimigo();
  }, 1000);
}







// ==========================================
// DEFENDER
// ==========================================


function defender(){



jogador.defesa=true;


ganharEnergia(
jogador,
10
);


escrever(
"🛡 O Arauto criou uma defesa."
);


finalizarTurnoJogador("Defesa");



}







// ==========================================
// POÇÃO JOGADOR
// ==========================================





async function usarPocao() {
    if (jogador.pocoes <= 0) {
        escrever("❌ Sem poções.");
        return;
    }

    try {
        const resultado = await enviarItemUsado(
            jogador,
            "Poção"
        );

        if (!resultado || resultado.sucesso !== true) {
            escrever("❌ Não foi possível remover a poção do inventário.");
            return;
        }

        jogador.pocoes = resultado.quantidade;

        jogador.vida += 35;

        if (jogador.vida > jogador.vidaMaxima) {
            jogador.vida = jogador.vidaMaxima;
        }

        ganharEnergia(jogador, 10);

        atualizarInterface();

        await escrever("🧪 O Arauto recuperou vida.");

        await finalizarTurnoJogador("Item");

    } catch (erro) {
        escrever("❌ Não foi possível usar a poção.");
        console.error("Erro ao usar poção:", erro);
    }
}







// ==========================================
// TURNO INIMIGO
// ==========================================


async function turnoInimigo() {

    if (!jogoAtivo)
        return;

    await esperar(800);

    
    // EFEITO PERSISTENTE: QUEIMADURA
    if (inimigo.queimadura > 0) {

        await aplicarEfeitos(inimigo);

        if (inimigo.vida <= 0) {
            fimJogo();
            return;
        }
    }



    // SUPREMO
    if (inimigo.energia >= 100) {

        inimigo.energia = 0;
        inimigo.energiaBloqueada = true;
        inimigo.supremoUsado = true;

        await escrever(
            "💀 Nêmesis liberou: FIM DA CRIAÇÃO!"
        );

        let dano = calcularDano(
            inimigo,
            jogador,
            ataquesInimigo.supremo.dano
        );

        causarDano(jogador, dano);

        await escrever(
            "💥 -" + dano + " HP"
        );

        atualizarInterface();

        await finalizarTurnoInimigo("Supremo");

        return;
    }

    // POÇÃO
    if (inimigo.vida < 70 && inimigo.pocoes > 0) {

        inimigo.pocoes--;

        try {
            await enviarItemUsado(
                inimigo,
                "Poção"
            );
        } catch (erro) {
            console.error(
                "Erro ao registrar a poção do inimigo:",
                erro
            );
        }

        inimigo.vida += 35;

        if (inimigo.vida > inimigo.vidaMaxima)
            inimigo.vida = inimigo.vidaMaxima;

        await escrever(
            "🧪 Nêmesis usou uma poção."
        );

        atualizarInterface();

        await esperar(1000);

        await finalizarTurnoInimigo("Item");

        return;
    }

    // DEFESA
    if (Math.random() < 0.15) {

        inimigo.defesa = true;

        await escrever(
            "🛡 Nêmesis criou uma barreira!"
        );

        await finalizarTurnoInimigo("Defesa");

        return;
    }

    // ATAQUE NORMAL
    let lista = [
        "colapso",
        "eclipse",
        "julgamento",
        "aniquilacao"
    ];

    let tipo =
        lista[
            Math.floor(Math.random() * lista.length)
        ];

    let ataque = ataquesInimigo[tipo];

    await escrever(
        "🌑 Nêmesis usou " + ataque.nome
    );

    let dano = calcularDano(
        inimigo,
        jogador,
        ataque.dano
    );

    causarDano(jogador, dano);

    await escrever(
        "💥 -" + dano + " HP"
    );

    // GANHAR ENERGIA
    inimigo.energia += ataque.energia;

    if (inimigo.energia > inimigo.energiaMaxima) {
        inimigo.energia = inimigo.energiaMaxima;
    }

    await escrever(
        "⚡ Nêmesis ganhou " + ataque.energia +
        " energia. Total: " + inimigo.energia
    );

    atualizarInterface();

    // Salva o turno uma única vez, com as vidas atualizadas.
    await finalizarTurnoInimigo("Ataque");
}



async function finalizarTurnoInimigo(tipoAcao) {

    try {
        await enviarStatusTurno(
            tipoAcao,
            inimigo.nome
        );
    } catch (erro) {
        console.error("Erro ao salvar turno do inimigo:", erro);
    }

    turno = "jogador";
    textoTurno.innerHTML = "Turno: " + jogador.nome;

    ativarBotoes();
}

// ==========================================
// HISTÓRIA E SINOPSE
// ==========================================


const introducao=[

"As montanhas estremecem.",

"O céu perde sua luz.",

"Uma presença ancestral desperta.",

"Seu poder faz o mundo tremer.",

"Entre milhões de vidas...",

"Somente um homem ousou desafiar",

"aquele que desejava apagar toda existência."

];



const sinopse=[

"Durante séculos, a humanidade explorou a natureza sem limites.",

"Florestas desapareceram.",

"Rios secaram.",

"O equilíbrio finalmente foi rompido.",

"O antigo Guardião da Natureza despertou.",

"Agora conhecido como Nêmesis Primordial.",

"Seu objetivo é eliminar toda civilização.",

"Você é o Arauto da Rebelião.",

"A última esperança da humanidade."

];








async function mostrarHistoria() {
  esconderTelas();
  historia.classList.remove("escondido");
  irParaTopo();

  textoHistoria.innerHTML = "";

  for (let frase of introducao) {
    textoHistoria.innerHTML += "<p>" + frase + "</p>";
    await esperar(1200);
  }

  textoHistoria.innerHTML += "<hr>";

  for (let frase of sinopse) {
    textoHistoria.innerHTML += "<p>" + frase + "</p>";
    await esperar(1200);
  }

  await esperar(1000);
  iniciarBatalha();
}


function mostrarSinopse() {
  esconderTelas();
  historia.classList.remove("escondido");
  irParaTopo();

  textoHistoria.innerHTML = "";

   for (let frase of sinopse) {
    textoHistoria.innerHTML += "<p>" + frase + "</p>";
  }
}






async function mostrarSinopse(){


esconderTelas();


historia.classList.remove("escondido");


irParaTopo();



textoHistoria.innerHTML="";



for(let frase of sinopse){

textoHistoria.innerHTML+=
"<p>"+frase+"</p>";

await esperar(1200);

}


}






// ==========================================
// INICIAR BATALHA
// ==========================================



async function iniciarBatalha() {

    // 1. Carrega os dados do banco de dados
    try {
        await carregarPersonagens();
    } catch (erro) {
        console.error("Não foi possível iniciar a batalha:", erro);
        alert("Não foi possível carregar os personagens. Verifique o Node-RED e tente novamente.");
        return;
    }

    // 2. Prepara a tela
    esconderTelas();
    jogo.classList.remove("escondido");
    irParaTopo();
    mensagens.innerHTML = "";

    // 3. Ativa o jogo
    jogoAtivo = true;
    atualizarInterface();

    // 4. Apresenta a batalha
    await escrever("⚔ O destino do mundo será decidido.");
    await escrever(jogador.nome + " VS " + inimigo.nome);
    await escrever("A batalha começou!");

    
    // 5. Sorteia quem começa
    desativarBotoes();

    if (Math.random() < 0.5) {
        turno = "jogador";
        textoTurno.innerHTML = "Turno: " + jogador.nome;
        ativarBotoes();
    } else {
        turno = "inimigo";
        textoTurno.innerHTML = "Turno: " + inimigo.nome;

        setTimeout(() => {
            turnoInimigo();
        }, 1000);
    }

}







// ==========================================
// ATAQUE SUPREMO
// ==========================================



async function ataqueSupremoJogador() {

    if (!jogoAtivo || turno !== "jogador") {
        return;
    }

    if (jogador.energia < 100) {
        await escrever("⚡ Energia insuficiente.");
        return;
    }

    if (jogador.supremoUsado) {
        await escrever("❌ Supremo já utilizado.");
        return;
    }

    desativarBotoes();

    jogador.supremoUsado = true;
    jogador.energia = 0;
    jogador.energiaBloqueada = true;

    await escrever("☀ AURORA DA HUMANIDADE!");

    let dano = calcularDano(
        jogador,
        inimigo,
        ataquesJogador.supremo.dano
    );

    causarDano(inimigo, dano);

    await escrever("💥 -" + dano + " HP");

    ganharEnergia(jogador, 0);

    if (inimigo.vida <= 0) {
        try {
            await enviarStatusTurno("Supremo", jogador.nome);
        } catch (erro) {
            console.error(
                "Erro ao salvar o supremo final:",
                erro
            );
        }

        fimJogo();
        return;
    }

    await finalizarTurnoJogador("Supremo");
}








// ==========================================
// EFEITOS
// ==========================================




async function aplicarEfeitos(p) {

    if (p.queimadura > 0) {

        p.queimadura--;

        p.vida -= 6;

        if (p.vida < 0) {
            p.vida = 0;
        }

        await escrever(
            "🔥 Queimadura causou 6 de dano em " +
            p.nome + "!"
        );

        atualizarInterface();

        try {
            await enviarStatusTurno("Efeito", p.nome);
        } catch (erro) {
            console.error(
                "Erro ao registrar o dano da queimadura:",
                erro
            );
        }
    }
}







async function enviarEfeito(personagem, efeito, rounds) {
  const resposta = await fetch("http://localhost:1880/api/efeito", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      partidaId: Number(partidaId),
      personagem: personagem.nome,
      efeito: efeito,
      rounds: rounds
    }),
    signal: AbortSignal.timeout(10000)
  });

  if (!resposta.ok) {
    throw new Error("Erro ao salvar efeito: " + resposta.status);
  }

  return await resposta.json();
}





// ==========================================
// FIM DE JOGO
// ==========================================


function fimJogo(){


if(inimigo.vida<=0){

    inimigo.vida=0;

    jogoAtivo=false;

    desativarBotoes();

    escrever(
        "🏆 Nêmesis Primordial foi derrotado!"
    );

    salvarBatalha("Arauto da Rebelião");

    return;
}





if(jogador.vida<=0){

    jogador.vida=0;

    jogoAtivo=false;

    desativarBotoes();

    escrever(
        "☠ O Arauto caiu em batalha."
    );

    salvarBatalha(inimigo.nome);

}




atualizarInterface();



}


async function salvarBatalha(vencedor) {
    const dados = {
        partidaId: Number(partidaId),
        jogador: jogador.nome,
        inimigo: inimigo.nome,
        vencedor: vencedor,
        vidaJogador: jogador.vida,
        vidaInimigo: inimigo.vida
    };

    if (!Number.isInteger(dados.partidaId) || dados.partidaId <= 0) {
        console.error("ID da partida inválido:", partidaId);
        return;
    }

    try {
        console.log("Dados enviados ao finalizar a batalha:", dados);

        const resposta = await fetch(
            "http://localhost:1880/api/batalha",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(dados)
            }
        );

        const resultado = await resposta.json();

        if (!resposta.ok || !resultado.sucesso) {
            console.error("Erro ao finalizar a partida:", resultado);
            return;
        }

        console.log("Partida finalizada com sucesso:", resultado);

    } catch (erro) {
        console.error("Erro ao comunicar com o Node-RED:", erro);
    }
}







// ==========================================
// CARREGAMENTO
// ==========================================


window.onload=function(){



menu=
document.getElementById("menu");


historia=
document.getElementById("historia");


jogo=
document.getElementById("jogo");


textoHistoria=
document.getElementById("textoHistoria");


mensagens=
document.getElementById("mensagens");



barraJogador=
document.getElementById("barraJogador");


barraInimigo=
document.getElementById("barraInimigo");



energiaJogadorBarra=
document.getElementById("energiaJogadorBarra");


energiaInimigoBarra=
document.getElementById("energiaInimigoBarra");



vidaJogador=
document.getElementById("vidaJogador");


vidaInimigo=
document.getElementById("vidaInimigo");



energiaJogador=
document.getElementById("energiaJogador");


energiaInimigo=
document.getElementById("energiaInimigo");



pocoesJogador=
document.getElementById("pocoesJogador");


pocoesInimigo=
document.getElementById("pocoesInimigo");



textoTurno=
document.getElementById("textoTurno");



document
.getElementById("btnRuina")
.onclick=
()=>usarAtaque("ruina");



document
.getElementById("btnJulgamento")
.onclick=
()=>usarAtaque("julgamento");



document
.getElementById("btnDestino")
.onclick=
()=>usarAtaque("destino");



document
.getElementById("btnAlvorecer")
.onclick=
()=>usarAtaque("alvorecer");



document
.getElementById("btnSupremo")
.onclick=
ataqueSupremoJogador;



document
.getElementById("btnDefender")
.onclick=
defender;



document
.getElementById("btnPocao")
.onclick=
usarPocao;

document
.getElementById("btnFugir")
.onclick = fugirBatalha;



esconderTelas();


menu.classList.remove("escondido");


atualizarInterface();



};



async function carregarPersonagens() {
    try {
        const resposta = await fetch(
            "http://localhost:1880/jogo/inicio/2"
        );

        if (!resposta.ok) {
            throw new Error(
                "Não foi possível carregar os dados da partida."
            );
        }

        const dados = await resposta.json();
        partidaId = Number(dados.partidaId);
        if (!Number.isInteger(partidaId) || partidaId <= 0) {
          throw new Error("O ID da partida não foi recebido corretamente.");
        }

        // JOGADOR
        jogador.id = dados.jogador.id;
        jogador.nome = dados.jogador.nome;
        jogador.vidaMaxima = Number(dados.jogador.hpMaximo);
        jogador.vida = Number(dados.jogador.hpAtual);
        jogador.itens = dados.jogador.itens || [];

        // INIMIGO
        inimigo.id = dados.inimigo.id;
        inimigo.nome = dados.inimigo.nome;
        inimigo.vidaMaxima = Number(dados.inimigo.hpMaximo);
        inimigo.vida = Number(dados.inimigo.hpAtual);
        inimigo.itens = dados.inimigo.itens || [];

        // QUANTIDADE DE POÇÕES DO JOGADOR
        jogador.pocoes = jogador.itens.reduce(
            (total, item) => {
                if (item.nome === "Poção") {
                    return total + Number(item.quantidade);
                }

                return total;
            },
            0
        );

        // QUANTIDADE DE POÇÕES DO INIMIGO
        inimigo.pocoes = inimigo.itens.reduce(
            (total, item) => {
                if (item.nome === "Poção") {
                    return total + Number(item.quantidade);
                }

                return total;
            },
            0
        );

        atualizarInterface();

        console.log("Personagens carregados:", dados);

    } catch (erro) {
        console.error("Erro ao carregar personagens:", erro);
        throw erro;
    }
}






async function enviarStatusTurno(tipoAcao, combatenteAtivo) {
    const personagemComEfeito =
        combatenteAtivo === jogador.nome ? jogador : inimigo;

    const resposta = await fetch(
        "http://localhost:1880/api/turno",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                partidaId: Number(partidaId),
                jogadorId: Number(jogador.id),
                oponenteId: Number(inimigo.id),

                jogador: jogador.nome,
                vidaJogador: jogador.vida,

                inimigo: inimigo.nome,
                vidaInimigo: inimigo.vida,

                combatenteAtivo: combatenteAtivo,
                tipoAcao: tipoAcao,

                efeitoPersistente:
                    tipoAcao === "Efeito" ? "queimadura" : null,

                alvoDanoPersistente:
                    tipoAcao === "Efeito"
                        ? personagemComEfeito.nome
                        : null,

                duracaoDanoPersistente:
                    tipoAcao === "Efeito"
                        ? personagemComEfeito.queimadura
                        : null
            })
        }
    );

    if (!resposta.ok) {
        throw new Error(
            "Erro ao salvar o turno: " + resposta.status
        );
    }

    return await resposta.json();
}







async function enviarItemUsado(personagem, item) {
    const resposta = await fetch(
        "http://localhost:1880/api/item/usado",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                personagem: personagem.nome,
                item: item
            })
        }
    );

    const resultado = await resposta.json();

    if (!resposta.ok || !resultado.sucesso) {
        throw new Error(
            resultado.mensagem || "Não foi possível usar o item."
        );
    }

    return resultado;
}



async function fugir() {
    if (!jogoAtivo || turno !== "jogador") {
        return;
    }

    desativarBotoes();

    await escrever("🏃 O Arauto da Rebelião fugiu da batalha!");

    jogoAtivo = false;
    turno = "";

    textoTurno.innerHTML = "Batalha encerrada";

    await escrever("Você voltou ao menu principal.");

    esconderTelas();
    menu.classList.remove("escondido");

    irParaTopo();
}

