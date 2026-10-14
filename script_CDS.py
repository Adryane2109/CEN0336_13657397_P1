#!/usr/bin/env python3

# Como o enunciado pede que o usuário forneça uma sequência de DNA
# e seis coordenadas pela linha de comando, importei o módulo sys.
import sys

# O nome do script também ocupa uma posição em sys.argv.
# Portanto, espero 8 elementos: o nome do script, a sequência e as seis coordenadas.
# Se a quantidade for diferente, informo ao usuário que faltam ou sobram argumentos.
if len(sys.argv) != 8:
    print("Erro: informe uma sequência de DNA e seis números inteiros.")

else:

    # Como o primeiro argumento corresponde à sequência de DNA, guardei seu conteúdo na variável sequencia.
    sequencia = sys.argv[1]

    # Como os outros seis argumentos devem ser números inteiros, usei isdigit() para verificar se o que foi informado contêm apenas dígitos.
    # Usei or porque basta um dos argumentos ser inválido para que a condição seja verdadeira.
    if (not sys.argv[2].isdigit() or
        not sys.argv[3].isdigit() or
        not sys.argv[4].isdigit() or
        not sys.argv[5].isdigit() or
        not sys.argv[6].isdigit() or
        not sys.argv[7].isdigit()):

        print("Erro: n1, n2, n3, n4, n5 e n6 devem ser números inteiros.")

    else:

        # Como os argumentos da linha de comando são recebidos como strings, usei int() para transformar as seis coordenadas em números inteiros.
        n1 = int(sys.argv[2])
        n2 = int(sys.argv[3])
        n3 = int(sys.argv[4])
        n4 = int(sys.argv[5])
        n5 = int(sys.argv[6])
        n6 = int(sys.argv[7])

        # Como as coordenadas indicam posições dentro da sequência, verifiquei se alguma delas ultrapassa o tamanho da sequência.
        # Usei len() para descobrir a quantidade de nucleotídeos da sequência informada.
        if (n1 > len(sequencia) or
            n2 > len(sequencia) or
            n3 > len(sequencia) or
            n4 > len(sequencia) or
            n5 > len(sequencia) or
            n6 > len(sequencia)):

            print("Erro: as coordenadas não podem ser maiores que o tamanho da sequência.")

        else:
            cds1 = sequencia[n1-1:n2]
            cds2 = sequencia[n3-1:n4]
            cds3 = sequencia[n5-1:n6]

            # Para verificar os introns, extraí as regiões entre o final de uma CDS e o início da CDS seguinte.
            # Como n2 e n4 são as últimas posições das CDS anteriores, usei esses valores como índices iniciais dos introns.
            # Como n3 e n5 são as primeiras posições das próximas CDS, subtraí 1 para não incluir essas posições nos introns.
            intron1 = sequencia[n2:n3-1]
            intron2 = sequencia[n4:n5-1]

            # O enunciado exige que os dois introns comecem com GT e terminem com AG.
            # Usei startswith() para verificar o início e endswith() para verificar o final de cada sequência.
            # Usei and porque todas as quatro condições precisam ser verdadeiras.
            if (intron1.startswith("GT") and
                intron1.endswith("AG") and
                intron2.startswith("GT") and
                intron2.endswith("AG")):

                # Como o resultado deve conter apenas as regiões codificantes, juntei as três CDS, deixando os introns de fora.
                cdna = cds1 + cds2 + cds3

                # Imprimi a sequência resultante
                print(cdna)

            # Se algum dos introns não começar com GT ou não terminar com AG, informo ao usuário que a condição do enunciado não foi atendida.
            else:
                print("Erro: as regiões entre as CDS não possuem GT no início e AG no final.")
