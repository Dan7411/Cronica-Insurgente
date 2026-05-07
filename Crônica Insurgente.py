import time
time.sleep(5)


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
print("Rebelião : 45 de dano")

print("Espíritos do Imortal")

print("#Distorção: HP = 95")
print("Ataques")
print("Irreal: 35")
print("Quebra: 40 de dano")

print("#Ascenção: HP = 100")
print("Expansão: 50 de dano")
print("Romper: 25 de dano")

print("Vida: HP = 90") 
print("Proteger: anula o ataque adversária, podendo ser usado uma vez")
print("Morte: 60 de dano")

rebeliao = int(90)

expurgo = int(50)
rebelião = int(60)

distorcao = int (95)
quebra = int(40)

ascencao = int(100)
expansao = int(50)
romper = int(25)

vida = int(90)
protect = int(-90)
morte = int(60)

# opcao 1
Hpr = rebeliao - quebra
hpd = distorcao - expurgo

# opcao 2
hpr = rebeliao - expansao
hpa = ascencao - rebelião

# opcao 3
hpr1 = rebeliao - morte
hpv = vida - expurgo

print("1 é distorção, 2 é ascenção e 3 é vida")

opcao1 = 1
opcao2 = 2
opcao3 = 3

expurgo = 1
rebelião = 2
 
opcao = int(input("Digite qual espírito o Imortal irá usar "))
ataque = int(input("qual ataque irá usar"))
match opcao, ataque:
    case 1:
        print("Você escolheu enfretar Distorção")
        print("Rebelião à Divindade usou expurgo contra Distorção")
        print("Distorção usou quebrar contra Rebelião à Divindade")
        print(f"Rebelião à Divindade ficou com {rebeliao - quebra} de HP")
        print(f"Distorção ficou com {distorcao - expurgo}")
        if Hpr > hpd:
            print("Rebelião à Divindade venceu")
            print("Distorção perdeu")
        else:
            print("Distorção venceu")
            print("Rebelião à divindade perdeu")
            
    case 2:
        print("Rebelião à Divindade usou rebelião contra Ascenção")
        print("Ascenção usou expansão contra Rebelião à Divindade")
        print(f"Rebelião á Divindade ficou com {rebeliao - expansao}")
        if hpr > hpa:
            print("Rebelião à Divindade venceu")
            print("Ascenção perdeu")
        else:
            print("Ascenção venceu")
            print("Rebelião à divindade perdeu")
        
    case 3:
        print("Rebelião à Divindade usou expurgo contra Vida")
        print("Vida usou morte contra Rebelião à Divindade")
        print(f"Rebelião à Divindade ficou com {rebeliao - morte} de HP")
        print(f"Vida ficou com {vida - expurgo}")
        if hpr1 > hpv:
            print("Rebelião à Divindade venceu")
            print("Vida perdeu")
        else:
            print("Vida venceu")
            print("Rebelião à divindade perdeu")

            
