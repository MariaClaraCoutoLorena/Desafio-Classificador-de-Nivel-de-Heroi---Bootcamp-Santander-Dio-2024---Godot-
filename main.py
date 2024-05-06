nome = input("Bem vindo herói, qual seu nome? ")
print("Que bom ter você conosco, ",nome,". Poderia me informar seu xp, por favor?", sep="", end=" ")
xp = int(input())
if xp<1001:
    nivel = "Ferro"
elif xp<2001:
    nivel = "Bronze"
elif xp<5001:
    nivel = "Prata"
elif xp<7001:
    nivel = "Ouro"
elif xp<8001:
    nivel = "Platina"
elif xp<9001:
    nivel = "Ascendente"
elif xp<10001:
    nivel = "Imortal"
else:
    nivel = "Radiante"
print("Que legal! Você está no nível ", nivel, ". Parabéns!", sep="")
