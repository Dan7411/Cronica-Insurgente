// ==========================================
// CRÔNICA INSURGENTE - SCRIPT COMPLETO
// PARTE 1
// ==========================================


// ==========================================
// VARIÁVEIS GLOBAIS
// ==========================================

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

    supremoUsado:false

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

    supremoUsado:false

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




async function escrever(texto){

    const linha=document.createElement("p");

    mensagens.appendChild(linha);


    for(let letra of texto){

        linha.innerHTML+=letra;

        await esperar(velocidadeTexto);

    }


    mensagens.scrollTop=mensagens.scrollHeight;

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

    personagem.energia += quantidade;

    if(personagem.energia > personagem.energiaMaxima){
        personagem.energia = personagem.energiaMaxima;
    }

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




if(ataque.efeito=="queimadura"){


inimigo.queimadura=3;


await escrever(
"🔥 Nêmesis sofreu queimadura!"
);


}



ganharEnergia(
jogador,
ataque.energia
);



if(inimigo.vida<=0){

fimJogo();

return;

}



finalizarTurnoJogador();



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


finalizarTurnoJogador();



}







// ==========================================
// POÇÃO JOGADOR
// ==========================================



function usarPocao(){


if(jogador.pocoes<=0){

escrever("❌ Sem poções.");

return;

}



jogador.pocoes--;


jogador.vida+=35;



if(jogador.vida>jogador.vidaMaxima)

jogador.vida=jogador.vidaMaxima;



ganharEnergia(
jogador,
10
);



atualizarInterface();



escrever(
"🧪 O Arauto recuperou vida."
);



finalizarTurnoJogador();



}






// ==========================================
// TURNO INIMIGO
// ==========================================


async function turnoInimigo(){


if(!jogoAtivo)
return;



await esperar(800);

// SUPREMO

if(inimigo.energia >= 100){

    inimigo.energia = 0;

    await escrever(
    "💀 Nêmesis liberou: FIM DA CRIAÇÃO!"
    );


    let dano = calcularDano(
        inimigo,
        jogador,
        ataquesInimigo.supremo.dano
    );


    causarDano(jogador,dano);


    await escrever(
    "💥 -" + dano + " HP"
    );


    atualizarInterface();


    finalizarTurnoInimigo();

    return;
}

// POÇÃO

if(
inimigo.vida<70 &&
inimigo.pocoes>0 &&
Math.random()<0.6
){


inimigo.pocoes--;


inimigo.vida+=35;


if(inimigo.vida>inimigo.vidaMaxima)

inimigo.vida=inimigo.vidaMaxima;



await escrever(
"🧪 Nêmesis usou uma poção!"
);



finalizarTurnoInimigo();

return;


}




// DEFESA

if(Math.random()<0.15){


inimigo.defesa=true;


await escrever(
"🛡 Nêmesis criou uma barreira!"
);



finalizarTurnoInimigo();

return;


}





// ATAQUE NORMAL


let lista=[

"colapso",
"eclipse",
"julgamento",
"aniquilacao"

];



let tipo=
lista[
Math.floor(Math.random()*lista.length)
];



let ataque=ataquesInimigo[tipo];



await escrever(
"🌑 Nêmesis usou "+ataque.nome
);



let dano=calcularDano(

inimigo,

jogador,

ataque.dano

);



causarDano(jogador,dano);


await escrever(
"💥 -"+dano+" HP"
);


// GANHAR ENERGIA
inimigo.energia += ataque.energia;

if(inimigo.energia > inimigo.energiaMaxima){
    inimigo.energia = inimigo.energiaMaxima;
}


await escrever(
"⚡ Nêmesis ganhou " + ataque.energia + 
" energia. Total: " + inimigo.energia
);


atualizarInterface();


finalizarTurnoInimigo();


}




function finalizarTurnoJogador(){


turno="inimigo";


textoTurno.innerHTML=
"Turno: "+inimigo.nome;



setTimeout(
turnoInimigo,
1000
);


}




function finalizarTurnoInimigo(){


turno="jogador";


textoTurno.innerHTML=
"Turno: "+jogador.nome;


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






async function mostrarHistoria(){


esconderTelas();


historia.classList.remove("escondido");


irParaTopo();


textoHistoria.innerHTML="";



for(let frase of introducao){

textoHistoria.innerHTML+=
"<p>"+frase+"</p>";

await esperar(1200);

}



textoHistoria.innerHTML+="<hr>";



for(let frase of sinopse){

textoHistoria.innerHTML+=
"<p>"+frase+"</p>";

await esperar(1200);

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


async function iniciarBatalha(){


esconderTelas();


jogo.classList.remove("escondido");



irParaTopo();



mensagens.innerHTML="";



jogoAtivo=true;



jogador.vida=jogador.vidaMaxima;

inimigo.vida=inimigo.vidaMaxima;



atualizarInterface();



await escrever(
"⚔ O destino do mundo será decidido."
);


await escrever(
jogador.nome+" VS "+inimigo.nome
);


await escrever(
"A batalha começou!"
);



if(Math.random()<0.5){


turno="jogador";


textoTurno.innerHTML=
"Turno: "+jogador.nome;


ativarBotoes();


}


else{


turno="inimigo";


textoTurno.innerHTML=
"Turno: "+inimigo.nome;


desativarBotoes();


setTimeout(
turnoInimigo,
1000
);


}


}







// ==========================================
// ATAQUE SUPREMO
// ==========================================


async function ataqueSupremoJogador(){



if(jogador.energia<100){

escrever(
"⚡ Energia insuficiente."
);

return;

}



if(jogador.supremoUsado){

escrever(
"❌ Supremo já utilizado."
);

return;

}



jogador.supremoUsado=true;

jogador.energia=0;



await escrever(
"☀ AURORA DA HUMANIDADE!"
);



let dano=
calcularDano(
jogador,
inimigo,
ataquesJogador.supremo.dano
);



causarDano(
inimigo,
dano
);



await escrever(
"💥 -"+dano+" HP"
);



fimJogo();



}







// ==========================================
// EFEITOS
// ==========================================


function aplicarEfeitos(p){



if(p.queimadura>0){


p.queimadura--;


p.vida-=6;


escrever(
"🔥 Queimadura causou 6 dano."
);


}



if(p.vida<0)

p.vida=0;



atualizarInterface();


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
"🏆 Nêmesis Primordial foi derrotada!"
);



return;


}




if(jogador.vida<=0){



jogador.vida=0;


jogoAtivo=false;


desativarBotoes();



escrever(
"☠ O Arauto caiu em batalha."
);



}



atualizarInterface();



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



esconderTelas();


menu.classList.remove("escondido");


atualizarInterface();



};