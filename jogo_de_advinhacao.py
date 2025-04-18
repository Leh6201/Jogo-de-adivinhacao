# Jogo de Adivinhação

import random

# Gerar um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

tentativas = 0
print("\nBem-vindo ao jogo de adivinhação!")

while True:
    chute = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s)!")
        break
    elif chute < numero_secreto:
        print("Tente um número maior...")
    else:
        print("Tente um número menor...")

