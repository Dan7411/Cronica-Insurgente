import time
time.sleep(2)

import random


#===========================

#       APRESENTAÇÃO

#===========================



print("---------[CRÔNICA INSURGENTE]---------")

print("Bem vindo viajante")
print("Nesse projeto, você jogará como o transcedente")
print("Usando sua vontade(a vontade do personagem é representada por um palavra) para lutar contra a do Imortal")
print("OBS:Esse é um jogo de combate por turnos")

input("Aperte enter para continuar: ")

print("Sipnose:\nUm mundo devastado pela miséria e discordia")
print("Nem sempre foi assim, tudo era colorido e abundante de vida.\nmas os, humanos, eles tinham uma ganância sem fim.")
print("Durante uma das várias extrações de recursos naturais deles,\ndespertaram o Imortal - antigo guardião da natureza, adormecido")
print("E o trancendente, aquele que foi criado só para impedir que a humanidade seja exterminada")

input("\nAperte enter para continuar: ")


#===========================

#     DICIONÁRIO DE VONTADES

#===========================



jogador = {
    "nome" : "Rebelião",
    "vida_atual": "95",
    "vida_máxima" : "95",
    "poções" : "2",
    "ataques" : ("Expurgo, Rebelião")
}

inimigo = {
    "nome" : "Divindade",
    "vida_atual": "100",
    "vida_máxima" : "100",
    "poções" : "1",
    "ataques" : ("Romper, Distorção")
}



#   =====================

#   DICIONÁRIO DE ATAQUES

#   =====================



ataque = {
    
    #ataque multi dano
    "rebeliao" : {
        
        "tipo" : "multi dano",
        "golpes" : "1-5",
        "dano" : "5"
    },
    
    #ataque dano contínuo
    "expurgo" : {
        
        "tipo" : "dano contínuo",
        "duração" : "3 turnos",
        "dano" : "15"   
    },

    #variável do dano contínuo
    "dano_contínuo" : {
        
        "ativo" : False,
        "dano" : "10",
        "duração" : "3"
    },

    #ataques inimigos
    "romper": {
        "tipo" : "normal",
        "dano" : "10"
    } ,
    "distorcao": {
        "tipo" : "normal",
        "dano" : "15"
    } ,

}



#========================


#    DICIONÁRIO DE POÇÕES


#=======================


poçoes = {
    "pocao pequena" : {
        "cura" : "20" 
    },

    "pocao grande" : {
        "cura" : "20"
    }
}


#==================


#FLUXO DA PARTIDA


#===================

#---STATUS INICIAL---


print(
    f"\n{jogador['nome']} -> "
    f"{jogador['vida_atual']} HP"
)

print(
    f"{inimigo['nome']} -> "
    f"{inimigo['vida_atual']} HP"
)


#---INÍCIO DO COMBATE---


primeiro_turno = random.choice([
    jogador["nome"],
    inimigo["nome"]
])

print(f"\nO {primeiro_turno} atacará primeiro")

while jogador['vida_máxima'] > 0 and inimigo['vida_máxima'] > 0:












