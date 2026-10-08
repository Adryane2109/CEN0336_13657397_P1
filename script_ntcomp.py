#!/usr/bin/env python3

# Pede ao usuário uma sequência de DNA
sequencia = input("Digite uma sequência de DNA: ")

# Verifica se a sequência contém somente A, T, C e G
valida = True

for base in sequencia:
    if base not in "ATCG":
        valida = False

# Se a sequência não for válida, mostra uma mensagem de erro
if not valida:
    print("Erro: a sequência deve conter apenas A, T, C e G (em letra maiuscula).")

else:

# Inicializa os contadores de cada nucleotídeo
    contador_A = 0
    contador_T = 0
    contador_C = 0
    contador_G = 0

# Percorre a sequência e conta cada nucleotídeo
    for base in sequencia:
        if base == "A":
            contador_A += 1
        elif base == "T":
            contador_T += 1
        elif base == "C":
            contador_C += 1
        elif base == "G":
            contador_G += 1

# Exibe a quantidade de cada nucleotídeo
    print("A:", contador_A)
    print("T:", contador_T)
    print("C:", contador_C)
    print("G:", contador_G)
