// ==================================
// CRÔNICA INSURGENTE
// SCRIPT.JS - PARTE 1
// ==================================


// ==================================
// PERSONAGENS
// ==================================

const jogador = {

    nome: "Insurgente Divino",

    vidaMaxima: 130,

    vida: 130,

    pocoes: 2,

    defesa: false,

    queimadura: 0

};



const inimigo = {

    nome: "Nêmesis Primordial",

    vidaMaxima: 145,

    vida: 145,

    pocoes: 2,

    defesa: false,

    queimadura: 0

};



// ==================================
// ATAQUES
// ==================================

const ataques = {


    ruina:{

        nome:"Ruína Celestial",

        dano:10,

        efeito:null

    },


    julgamento:{

        nome:"Julgamento da Rebelião",

        dano:16,

        efeito:"queimadura"

    },


    colapso:{

        nome:"Colapso do Destino",

        dano:12,

        efeito:null

    },


    eclipse:{

        nome:"Eclipse da Realidade",

        dano:9,

        efeito:"duplo"

    }

};



// ==================================
// VARIÁVEIS DO JOGO
// ==================================

let jogoAtivo = false;

let turno = "";



// ==================================
// SISTEMA DE MENSAGEM
// ==================================

function mensagem(texto){


    const terminal =
    document.getElementById("mensagens");


    terminal.innerHTML +=
    "<p>" + texto + "</p>";


    terminal.scrollTop =
    terminal.scrollHeight;

}



// pausa entre mensagens

function esperar(tempo){

    return new Promise(resolve =>{

        setTimeout(resolve,tempo);

    });

}



// mensagem com intervalo

async function mensagemLenta(texto){

    mensagem(texto);

    await esperar(700);

}



// ==================================
// TROCA DE TELAS
// ==================================

function esconderTudo(){


    document.getElementById("menu")
    .classList.add("escondido");


    document.getElementById("historia")
    .classList.add("escondido");


    document.getElementById("jogo")
    .classList.add("escondido");


}



function mostrarHistoria(){


    esconderTudo();


    document.getElementById("historia")
    .classList.remove("escondido");


    document.getElementById("textoHistoria")
    .innerHTML = `

    As montanhas estremecem...

    <br><br>

    O céu perdeu sua luz.

    <br><br>

    Uma presença ancestral desperta.

    <br><br>

    Seu poder faz o próprio mundo
    tremer diante da destruição.

    <br><br>

    Entre milhões de vidas,
    apenas um cultivador ousou desafiar
    aquele que se proclamou uma divindade.

    <br><br>

    Durante séculos, a humanidade explorou
    a natureza sem limites.

    <br><br>

    Florestas desapareceram.
    Rios secaram.
    Montanhas foram reduzidas a cinzas.

    <br><br>

    Quando o equilíbrio foi rompido,
    o Guardião da Natureza despertou.

    <br><br>

    Agora conhecido como
    <b>Nêmesis Primordial</b>,
    ele decidiu julgar a humanidade.

    <br><br>

    Você é o último transcendente.

    O destino do mundo depende da sua força.

    `;

}



// ==================================
// MOSTRAR SINOPSE
// ==================================

function mostrarSinopse(){


    esconderTudo();


    document.getElementById("historia")
    .classList.remove("escondido");


    document.getElementById("textoHistoria")
    .innerHTML = `


    📜 <b>Sinopse</b>

    <br><br>


    A humanidade abusou da natureza
    durante séculos.

    <br><br>

    Quando o equilíbrio finalmente acabou,
    uma força ancestral despertou.

    <br><br>

    O mundo agora está diante de seu julgamento.

    <br><br>

    Apenas o Insurgente Divino pode impedir
    o fim da civilização.

    `;


}

// ==================================
// INICIAR BATALHA
// ==================================

async function iniciarBatalha(){

    esconderTudo();


    document.getElementById("jogo")
    .classList.remove("escondido");


    jogoAtivo = true;


    await mensagemLenta(
        "⚔ O confronto final começa..."
    );


    await mensagemLenta(
        "⚔ INSURGENTE DIVINO"
    );


    await mensagemLenta(
        "O último transcendente que desafia uma força ancestral."
    );


    await mensagemLenta(
        "🌑 NÊMESIS PRIMORDIAL"
    );


    await mensagemLenta(
        "A manifestação do julgamento da natureza."
    );


    await mensagemLenta(
        "════════════════════"
    );


    atualizarInterface();


    // escolhe quem começa

    if(Math.random() < 0.5){


        turno = "jogador";


        await mensagemLenta(
            "🎭 O Insurgente Divino começa!"
        );


    }else{


        turno = "inimigo";


        await mensagemLenta(
            "🌑 Nêmesis Primordial começa!"
        );


        setTimeout(turnoInimigo,1000);


    }

}



// ==================================
// ATUALIZAR INTERFACE
// ==================================

function atualizarInterface(){


    // vida jogador

    document.getElementById("vidaJogador")
    .innerHTML =
    "❤️ Vida: "
    + jogador.vida
    + " / "
    + jogador.vidaMaxima;



    document.getElementById("vidaInimigo")
    .innerHTML =
    "❤️ Vida: "
    + inimigo.vida
    + " / "
    + inimigo.vidaMaxima;



    // poções


    document.getElementById("pocoesJogador")
    .innerHTML =
    "🧪 Poções: "
    + jogador.pocoes;



    document.getElementById("pocoesInimigo")
    .innerHTML =
    "🧪 Poções: "
    + inimigo.pocoes;



    // barras


    document.getElementById("barraJogador")
    .style.width =
    (jogador.vida /
    jogador.vidaMaxima * 100)
    + "%";



    document.getElementById("barraInimigo")
    .style.width =
    (inimigo.vida /
    inimigo.vidaMaxima * 100)
    + "%";

}



// ==================================
// DANO CRÍTICO
// ==================================

function calcularDano(dano){


    let critico = false;


    // 20% de chance

    if(Math.random() < 0.20){

        dano *= 2;

        critico = true;

    }



    return {

        dano:dano,

        critico:critico

    };


}



// ==================================
// APLICAR DANO
// ==================================

async function causarDano(
    alvo,
    dano,
    nomeAtaque
){


    let resultado =
    calcularDano(dano);



    dano =
    resultado.dano;



    if(resultado.critico){


        await mensagemLenta(
            "💥 ATAQUE CRÍTICO!"
        );


    }



    // defesa reduz metade

    if(alvo.defesa){


        dano =
        Math.floor(dano / 2);


        alvo.defesa = false;


        await mensagemLenta(
            "🛡 A defesa reduziu o dano!"
        );


    }



    alvo.vida -= dano;



    if(alvo.vida < 0){

        alvo.vida = 0;

    }



    await mensagemLenta(

        "💢 "
        + nomeAtaque
        + " causou "
        + dano
        + " de dano!"

    );


    await mensagemLenta(

        "❤️ Vida restante: "
        + alvo.vida

    );


    atualizarInterface();

}

// ==================================
// ATAQUES DO JOGADOR
// ==================================


async function usarAtaque(tipo){


    if(!jogoAtivo) return;


    if(turno !== "jogador"){

        return;

    }



    let ataque = ataques[tipo];



    await mensagemLenta(
        "⚔ Você usou "
        + ataque.nome
        + " ("
        + ataque.dano
        + " dano)"
    );



    await causarDano(

        inimigo,

        ataque.dano,

        ataque.nome

    );



    // efeito de queimadura

    if(ataque.efeito === "queimadura"){


        inimigo.queimadura = 3;



        await mensagemLenta(

            "🔥 Nêmesis Primordial foi queimado!"

        );

    }



    verificarFim();



    if(jogoAtivo){


        turno = "inimigo";


        setTimeout(turnoInimigo,1000);


    }


}




// ==================================
// DEFESA
// ==================================


async function defender(){


    if(!jogoAtivo) return;


    if(turno !== "jogador"){

        return;

    }



    jogador.defesa = true;



    await mensagemLenta(

        "🛡 Insurgente Divino entrou em posição defensiva!"

    );



    turno = "inimigo";


    setTimeout(turnoInimigo,1000);


}




// ==================================
// POÇÃO
// ==================================


async function usarPocao(){


    if(!jogoAtivo) return;


    if(turno !== "jogador"){

        return;

    }



    if(jogador.pocoes <= 0){


        await mensagemLenta(

            "❌ Você não possui mais poções!"

        );


        return;

    }



    jogador.pocoes--;



    let cura = 30;



    jogador.vida += cura;



    if(jogador.vida > jogador.vidaMaxima){


        jogador.vida =
        jogador.vidaMaxima;

    }



    await mensagemLenta(

        "🧪 Você usou uma Poção!"

    );



    await mensagemLenta(

        "❤️ Recuperou "
        + cura
        + " de vida!"

    );



    atualizarInterface();



    turno = "inimigo";


    setTimeout(turnoInimigo,1000);


}




// ==================================
// FUGIR
// ==================================


async function fugir(){


    if(!jogoAtivo) return;



    jogoAtivo = false;



    await mensagemLenta(

        "🏃 O Insurgente Divino abandonou a batalha."

    );



    bloquearBotoes();

}



// ==================================
// EFEITO DE QUEIMADURA
// ==================================


async function aplicarEfeitos(){



    if(inimigo.queimadura > 0){


        inimigo.vida -= 4;



        inimigo.queimadura--;



        await mensagemLenta(

            "🔥 Nêmesis sofreu 4 de dano da queimadura!"

        );



        atualizarInterface();


    }



    if(jogador.queimadura > 0){


        jogador.vida -= 4;



        jogador.queimadura--;



        await mensagemLenta(

            "🔥 Insurgente sofreu dano da queimadura!"

        );



        atualizarInterface();


    }


}

// ==================================
// TURNO DO INIMIGO
// ==================================

async function turnoInimigo(){


    if(!jogoAtivo) return;



    await mensagemLenta(
        "🌑 Turno da Nêmesis Primordial..."
    );



    await aplicarEfeitos();



    if(inimigo.vida <= 0){

        verificarFim();

        return;

    }



    let escolha = Math.random();



    // usa poção quando estiver com pouca vida

    if(
        inimigo.vida <= 50 &&
        inimigo.pocoes > 0 &&
        escolha < 0.25
    ){


        await pocaoInimigo();



    }



    // defesa

    else if(escolha < 0.45){


        await defesaInimigo();



    }



    // fuga rara

    else if(escolha < 0.48){


        await mensagemLenta(

            "🌑 A Nêmesis Primordial recuou da batalha..."

        );


        jogoAtivo = false;


        bloquearBotoes();


        return;


    }



    // ataque

    else{


        let ataquesInimigo = [

            ataques.colapso,

            ataques.eclipse

        ];



        let ataque =

        ataquesInimigo[
            Math.floor(
                Math.random()
                *
                ataquesInimigo.length
            )
        ];



        await ataqueInimigo(ataque);



    }



    verificarFim();



    if(jogoAtivo){


        turno = "jogador";


        await mensagemLenta(

            "🎭 Seu turno!"

        );


    }


}



// ==================================
// ATAQUE DO INIMIGO
// ==================================

async function ataqueInimigo(ataque){



    await mensagemLenta(

        "🌑 Nêmesis usou "
        + ataque.nome
        + " ("
        + ataque.dano
        + " dano)"

    );



    await causarDano(

        jogador,

        ataque.dano,

        ataque.nome

    );



    // efeito golpe duplo

    if(ataque.efeito === "duplo"){


        if(Math.random() < 0.40){


            await mensagemLenta(

                "⚡ O ataque atingiu novamente!"

            );



            await causarDano(

                jogador,

                ataque.dano,

                "Segundo impacto"

            );


        }


    }


}



// ==================================
// POÇÃO DO INIMIGO
// ==================================

async function pocaoInimigo(){


    inimigo.pocoes--;



    let cura = 35;



    inimigo.vida += cura;



    if(
        inimigo.vida >
        inimigo.vidaMaxima
    ){

        inimigo.vida =
        inimigo.vidaMaxima;

    }



    await mensagemLenta(

        "🌑 Nêmesis Primordial usou uma poção!"

    );



    await mensagemLenta(

        "❤️ Recuperou "
        + cura
        + " de vida."

    );



    atualizarInterface();


}



// ==================================
// DEFESA DO INIMIGO
// ==================================

async function defesaInimigo(){


    inimigo.defesa = true;



    await mensagemLenta(

        "🛡 Nêmesis Primordial criou uma barreira!"

    );


}

// ==================================
// VERIFICAR FIM DA BATALHA
// ==================================

function verificarFim(){


    if(inimigo.vida <= 0){


        jogoAtivo = false;


        mensagem(
            "🏆 VITÓRIA!"
        );


        mensagem(
            "O Nêmesis Primordial foi derrotado."
        );


        mensagem(
            "🌎 A humanidade ganhou uma nova chance."
        );


        bloquearBotoes();


        return true;

    }



    if(jogador.vida <= 0){


        jogoAtivo = false;


        mensagem(
            "☠ DERROTA!"
        );


        mensagem(
            "O Insurgente Divino caiu diante do julgamento."
        );


        mensagem(
            "🌑 A Nêmesis Primordial venceu."
        );


        bloquearBotoes();


        return true;

    }



    return false;


}



// ==================================
// BLOQUEAR BOTÕES
// ==================================

function bloquearBotoes(){


    let botoes =
    document.querySelectorAll(
        ".acoes button"
    );



    botoes.forEach(
        botao => {

            botao.disabled = true;

        }
    );

}



// ==================================
// REINICIAR BATALHA
// ==================================

function reiniciarJogo(){


    jogador.vida =
    jogador.vidaMaxima;


    inimigo.vida =
    inimigo.vidaMaxima;


    jogador.pocoes = 2;


    inimigo.pocoes = 2;


    jogador.defesa = false;


    inimigo.defesa = false;


    jogador.queimadura = 0;


    inimigo.queimadura = 0;


    jogoAtivo = true;


    atualizarInterface();


}



// ==================================
// ATIVAR BOTÕES NOVAMENTE
// ==================================

function ativarBotoes(){


    let botoes =
    document.querySelectorAll(
        ".acoes button"
    );



    botoes.forEach(
        botao => {

            botao.disabled = false;

        }
    );

}



// ==================================
// SOBRESCREVE INÍCIO DA BATALHA
// ==================================

const inicioOriginal =
iniciarBatalha;



iniciarBatalha = async function(){


    reiniciarJogo();


    ativarBotoes();


    esconderTudo();


    document
    .getElementById("jogo")
    .classList
    .remove("escondido");



    document
    .getElementById("mensagens")
    .innerHTML = "";



    await mensagemLenta(

        "⚔ A batalha entre forças opostas começou!"

    );



    await mensagemLenta(

        "⚔ Insurgente Divino VS 🌑 Nêmesis Primordial"

    );



    atualizarInterface();



    if(Math.random() < 0.5){


        turno = "jogador";


        await mensagemLenta(

            "🎭 Você começa o combate!"

        );


    }

    else{


        turno = "inimigo";


        await mensagemLenta(

            "🌑 Nêmesis Primordial começa!"

        );


        setTimeout(
            turnoInimigo,
            1000
        );


    }


}

