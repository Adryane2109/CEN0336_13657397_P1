#!/usr/bin/env python3

# Como o enunciado pede que o usuário forneça uma sequência de DNA, usei input() para receber essa sequência pelo terminal.
sequencia = input("Digite uma sequência de DNA: ")

# Como a sequência deve conter somente A, T, C e G,
# criei uma variável valida com o valor True para indicar inicialmente
# que a sequência é válida.
valida = True

# Para verificar todos os caracteres informados pelo usuário, usei um loop for para percorrer a sequência, uma base por vez.
for base in sequencia:
    # Se o caracter não pertencer a ATCG, sua invalidez é traduzida como False.
    if base not in "ATCG":
        valida = False

# Depois da verificação, se a sequência não for válida, mostra uma mensagem de erro
if not valida:
    print("Erro: a sequência deve conter apenas A, T, C e G (em letra maiuscula).")

else:

    # Como preciso contar quatro tipos diferentes de nucleotídeos,
    # criei uma variável para cada um deles e iniciei todas com zero,
    # pois nenhuma ocorrência foi contada ainda.
    contador_A = 0
    contador_T = 0
    contador_C = 0
    contador_G = 0

    # Como preciso descobrir quantas vezes cada base aparece,
    # percorro novamente a sequência usando um loop for. 
    # Se a base for aquela especificada pela variável, o código acrescenta 1 ao contador da respectiva variável.
    for base in sequencia:
        if base == "A":
            contador_A += 1
        elif base == "T":
            contador_T += 1
        elif base == "C":
            contador_C += 1
        elif base == "G":
            contador_G += 1

    # Depois de percorrer toda a sequência, uso print() para exibir a quantidade encontrada de cada nucleotídeo.
    print("A:", contador_A)
    print("T:", contador_T)
    print("C:", contador_C)
    print("G:", contador_G)
