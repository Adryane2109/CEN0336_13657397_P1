#!/usr/bin/env python3

# Como o enunciado pede que os números sejam fornecidos na linha de comando, importei o módulo sys, que permite acessar os argumentos recebidos pelo script.
import sys

# Como o nome do script também conta como um argumento em sys.argv,
# espero receber 3 elementos: o nome do script e os dois números inteiros.
# Se a quantidade de elementos for diferente de 3, exibo uma mensagem de erro ao usuário.
if len(sys.argv) != 3:
    print("Erro: informe dois números inteiros.")
else:

    # Como preciso trabalhar com números inteiros positivos,
    # usei isdigit() para verificar se os dois argumentos contêm apenas dígitos.
    # O operador or permite identificar se pelo menos um dos valores é inválido.
    if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        print("Erro: os dois valores devem ser números inteiros.")
    else:

        # Como os argumentos recebidos por sys.argv são strings,usei int() para converter os dois valores para o tipo inteiro.
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        # Pelo teorema de Pitágoras, o quadrado da hipotenusa é igual à soma dos quadrados dos dois catetos: a² + b².
        # Usei ** 2 para calcular o quadrado de cada número
        quadrado_hipotenusa = a**2 + b**2

        # Por fim, imprimi o resultado no formato solicitado pelo enunciado.
        # Usei str() para converter os números inteiros em strings, permitindo concatená-los com o restante do texto.
        print("O quadrado da hipotenusa para o triangulo retângulo com lados a=" + str(a) + " e b=" + str(b) + ", é " + str(quadrado_hipotenusa))
