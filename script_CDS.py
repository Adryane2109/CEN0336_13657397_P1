#!/usr/bin/env python3

# Importa o módulo sys para receber os argumentos
# fornecidos pelo usuário na linha de comando
import sys

# Confere se o usuário forneceu uma sequência
# e seis números inteiros
if len(sys.argv) != 8:
    print("Erro: informe uma sequência de DNA e seis números inteiros.")

else:

    # Guarda a sequência de DNA
    sequencia = sys.argv[1]

    # Confere se os seis argumentos são números inteiros
    if (not sys.argv[2].isdigit() or
        not sys.argv[3].isdigit() or
        not sys.argv[4].isdigit() or
        not sys.argv[5].isdigit() or
        not sys.argv[6].isdigit() or
        not sys.argv[7].isdigit()):

        print("Erro: n1, n2, n3, n4, n5 e n6 devem ser números inteiros.")

    else:

        # Converte as coordenadas de string para inteiro
        n1 = int(sys.argv[2])
        n2 = int(sys.argv[3])
        n3 = int(sys.argv[4])
        n4 = int(sys.argv[5])
        n5 = int(sys.argv[6])
        n6 = int(sys.argv[7])

        # Confere se nenhuma coordenada é maior que
        # o tamanho da sequência
        if (n1 > len(sequencia) or
            n2 > len(sequencia) or
            n3 > len(sequencia) or
            n4 > len(sequencia) or
            n5 > len(sequencia) or
            n6 > len(sequencia)):

            print("Erro: as coordenadas não podem ser maiores que o tamanho da sequência.")

        else:

            # Extrai as três CDS.
            # O -1 é usado porque as posições da questão
            # começam em 1 e os índices do Python começam em 0.
            cds1 = sequencia[n1-1:n2]
            cds2 = sequencia[n3-1:n4]
            cds3 = sequencia[n5-1:n6]

            # Extrai as regiões entre as CDS
            intron1 = sequencia[n2:n3-1]
            intron2 = sequencia[n4:n5-1]

            # Verifica se os dois introns começam com GT
            # e terminam com AG
            if (intron1.startswith("GT") and
                intron1.endswith("AG") and
                intron2.startswith("GT") and
                intron2.endswith("AG")):

                # Junta as três CDS
                cdna = cds1 + cds2 + cds3

                # Imprime a sequência resultante
                print(cdna)

            else:
                print("Erro: as regiões entre as CDS não possuem GT no início e AG no final.")
