#!/usr/bin/env python3

# Importa o módulo sys para receber os valores fornecidos pelo usuário na linha de comando
import sys

# Confere se o usuário forneceu dois valores inteiros
if len(sys.argv) != 3:
    print("Erro: informe dois números inteiros.")
else:

    # Confere se os dois valores são números
    if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        print("Erro: os dois valores devem ser números inteiros.")
    else:

        # Converte os valores de string para inteiros
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        # Calcula o quadrado da hipotenusa
        quadrado_hipotenusa = a**2 + b**2

        # Mostra o resultado na tela
        print("O quadrado da hipotenusa para o triangulo retângulo com lados a=" + str(a) + " e b=" + str(b) + ", é " + str(quadrado_hipotenusa))
