import time
time.sleep(2)


print("CRÔNICA INSURGENTE")

print("Bem vindo viajante")
print("Nesse projeto, você jogará como o transcedente")
print("Usando seu espírito para lutar com os do Imortal")
print("OBS:Esse é um jogo de combate por turnos")
print("Sipnose: Um mundo devastado pela miséria e discordia, mas nem sempre foi assim, o mundo era cheio de vida... Porém tinha um problema, humanos,  eles estavam destruindo tudo, até que um dia eles o acordaram - Imortal. Uma entidade selada por mestres de espírito, agora você é um mestres de espírito que veio do futuro, com o objetivo de derrotar o Imortal, antes que ele domine os humanos")

print("Espírito do Trancendente")

print("#Rebelião à Dinvidade: HP = 90")
print("Ataques")
print("Expurgo: 40 de dano")
print("Rebelião : 40 de dano")

print("Espírito do Imortal")

print("#Distorção: HP = 95")
print("Ataques")
print("Irreal: 40")
print("Quebra: 40 de dano")
#
#print("#Ascenção: HP = 100")
#print("Expansão: 50 de dano")
#print("Romper: 25 de dano")
#
#print("Vida: HP = 90") 
#print("Proteger: anula o ataque adversária, podendo ser usado uma vez")
#print("Morte: 60 de dano")

rebeliao = int(90)

expurgo = int(20)
rebelião = int(20)

distorcao = int (95)
quebra = int(20)
irreal = int(20)

#ascencao = int(100)
#expansao = int(50)
#romper = int(25)

#vida = int(90)
#protect = int(-90)
#morte = int(60)

# opcao 1
Hpr = rebeliao - quebra
hpd = distorcao - expurgo

# opcao 2
#h#pr = rebeliao - expansao
#hpa = ascencao - rebelião

# opcao 3
#hpr1 = rebeliao - morte
#h3pv = vida - expurgo

#print("1 é distorção, 2 é ascenção e 3 é vida")

##pcao2 = 2
#opcao3 = 3

hpr1 = rebeliao - expurgo
hpd1 = distorcao - expurgo

hpr2 = hpr1 - expurgo
hpd2 = hpd1 - expurgo

hpr3 = hpr2 - expurgo
hpd3 = hpd2 - expurgo

hpr4 = hpr3 - expurgo
hpd4 = hpd3 - expurgo

hpr5 = hpr4 - expurgo
hpd5 = hpd4 - expurgo


ataque1 = 1
ataque2 = 2
 
print("1 é o expugo, e 2 é rebelião")
#opcao = int(input("Digite qual espírito o Imortal irá usar "))
print("Distorção(95)")
print("Rebelião à Divindade(90)")

#match opcao:
#    case 1:

venceu = False

while venceu == False:
    ataque = int(input("qual ataque irá usar: "))
    print("Rebelião à Divindade usou expurgo contra Distorção")
    print("Distorção usou quebra contra Rebelião à Divindade")
    print(f"Rebelião à Divindade ficou com {hpr1} de HP")
    print(f"Distorção ficou com {hpd1}")
    
    if rebeliao <= 0:
        print("Você venceu")
        venceu = True   
    else:
        print("A batalha continua")          
    
    ataque = int(input("qual ataque irá usar: "))
    print("Rebelião à Divindade usou expurgo contra Distorção")
    print("Distorção usou quebra contra Rebelião à Divindade")
    print(f"Rebelião à Divindade ficou com {hpr2} de HP")
    print(f"Distorção ficou com {hpd3}")

    if  <= 0:
        print("Você venceu")
        venceu = True   
    else:
        print("A batalha continua")      
   
    ataque = int(input("qual ataque irá usar: "))
    print("Rebelião à Divindade usou expurgo contra Distorção")
    print("Distorção usou quebra contra Rebelião à Divindade")
    print(f"Rebelião à Divindade ficou com {} de HP")
    print(f"Distorção ficou com {derrota - expurgo - expurgo}")

    if divino = 0:
        print("Você venceu")
        venceu = True   
    else:
        print("A batalha continua") 
   
   



 #case 2:
    #    print("Rebelião à Divindade usou rebelião contra Ascenção")
    #    print("Ascenção usou expansão contra Rebelião à Divindade")
    #    print(f"Rebelião á Divindade ficou com {rebeliao - expansao}")
    #    if hpr > hpa:
    #        print("Rebelião à Divindade venceu")
    #        print("Ascenção perdeu")
    #    else:
    #        print("Ascenção venceu")
    #        print("Rebelião à divindade perdeu")
    #    
    #case 3:
    #    print("Rebelião à Divindade usou expurgo contra Vida")
    #    print("Vida usou morte contra Rebelião à Divindade")
    #    print(f"Rebelião à Divindade ficou com {rebeliao - morte} de HP")
    #    print(f"Vida ficou com {vida - expurgo}")
    #    if hpr1 > hpv:
    #        print("Rebelião à Divindade venceu")
    #        print("Vida perdeu")
    #    else:
    #        print("Vida venceu")
    #        print("Rebelião à divindade perdeu")
#
    #        
#