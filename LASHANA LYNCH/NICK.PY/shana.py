import random

print("JOKENPO")

comp = random.randint(0, 2)

# Escolha do computador
if comp == 0:
    print("Computador jogou: pedra")
elif comp == 1:
    print("Computador jogou: papel")
else:
    print("Computador jogou: tesoura")

jogador = int(input("Escolha 0 para pedra, 1 para papel ou 2 para tesoura: "))

if jogador == 0:
    print("Você jogou: pedra")
elif jogador == 1:
    print("Você jogou: papel")
else:
    print("Você jogou: tesoura")

# Verificando o vencedor
if (comp == jogador):
    print("EMPATE!")
elif (comp == 0 and jogador == 1) or (comp == 1 and jogador == 2) or (comp == 2 and jogador == 0):
    print("JOGADOR VENCEU!")
else:
    print("COMPUTADOR VENCEU!")

print("[0] pedra")
print("[1] papel")
print("[2] tesoura")