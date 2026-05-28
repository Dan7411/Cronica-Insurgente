import time
time.sleep(2)

import random


print("---------[CRÔNICA INSURGENTE]---------")

print("Bem vindo viajante")
print("Nesse projeto, você jogará como o transcedente")
print("Usando seu espírito para lutar com os do Imortal")
print("OBS:Esse é um jogo de combate por turnos")
print("Sipnose: Um mundo devastado pela miséria e discordia, mas nem sempre foi assim, o mundo era cheio de vida... Porém tinha um problema, humanos,  eles estavam destruindo tudo, até que um dia eles o acordaram - Imortal. Uma entidade selada por mestres de espírito, agora você é um mestres de espírito que veio do futuro, com o objetivo de derrotar o Imortal, antes que ele domine os humanos")

print("Espírito do Trancendente")

print("#Rebelião à Dinvidade: HP = 90")
print("Ataques")
print("Expurgo: 20 de dano")
print("Rebelião : 10 de dano")
#print("#Ascenção: HP = 100")
#print("Expansão: 50 de dano")
#print("Romper: 25 de dano")
#
#print("Vida: HP = 90") 
#print("Proteger: anula o ataque adversária, podendo ser usado uma vez")
#print("Morte: 60 de dano")

jogavel = {
  "nome : Rebelião à Divindade"
  "hp" : 90 ,
  "expurgo" : 20 ,
  "rebeliao" : 10 ,
  "marcado" : 0
  }



vida_inimigo = 95
#quebra = 20



ataque1 = 1
ataque2 = 2

turno = 0


print("A batalha começou!")

hp = 95
vida_inimigo = 95
selecao = True

while selecao == True:
    
    
    adversario = random.choice([1,2,3,4])
    at = {
    "um" : "10",
    "dois" : "20",
    "tres" : "30",
    "quatro" : "40"    
    }
    
    turno += 1
    print(f"----------TURNO{turno}---------- ")
    print("Rebelião à Divindade vs Ascenção")
    
    print("Qual ataque irá usar?")
    print("expurgo ou rebelião")
    ataque = int(input("Selecione o ataque:"))

    #if hp <= 0:
    #    selecao = False
    

       
    

    if ataque == 1:
        print("Rebelião à Divindade usou expurgo e causou 20 de dano ao adversário")
        print(f"Ascenção está com {vida_inimigo - jogavel["expurgo"]} de hp") 
        vida_inimigo -= 20
    
    elif ataque == 2:                    
         print("Rebelião à Divindade usou rebelião e causou 10 de dano ao adversário")
         print(f"Ascenção está com {vida_inimigo - jogavel["rebeliao"]} de hp")
         vida_inimigo -= 10

    elif adversario == 1:
          print(f"Ascenção usou quebra e causou {at["um"]} de dano")
          print(f"Rebelião à Divindade está com {hp - at["um"]}")
          hp -= 10
    
    elif adversario == 2:
          print(f"Ascenção usou quebra e causou {at["dois"]} de dano")
          print(f"Rebelião à Divindade está com {hp - at["dois"]}")
          hp -= 20
    
    elif adversario == 3:
          print(f"Ascenção usou quebra e causou {at["tres"]} de dano")
          print(f"Rebelião à Divindade está com {hp - at["tres"]}")
          hp -= 30

    elif adversario == 4:
          print(f"Ascenção usou quebra e causou {at["quatro"]} de dano")
          print(f"Rebelião à Divindade está com {hp - at["quatro"]}")
          hp -= 40

    elif adversario == 1:
       for dano in range(1,5):
         dano = 5
         print(f"irreal causou {dano} de dano")
         print(f"Rebelião à Divindade está com {hp - dano} de hp")
         hp -= dano


    elif hp <= 0:
        print("Que pena! Ascenção venceu")
        break
    elif vida_inimigo <= 0:
        print(f"Ascenção está com 0 de hp")
        print("Parabéns, Rebelião à Divindade venceu!")
        break

















































