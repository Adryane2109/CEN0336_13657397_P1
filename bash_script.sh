#!/bin/bash
# Primeiro, indiquei que o arquivo deve ser executado pelo interpretador Bash pois o enunciado pede a criação de um script de Bash para rodar no Linux.

# Para descobrir em qual diretório/pasta estou trabalhando, usei o comando pwd. Ele mostra o caminho completo do diretório atual.
pwd

# Como o enunciado pede uma lista detalhada do conteúdo da minha pasta HOME, usei o comando ls, que lista meus arquivos e diretórios.
# Acrescentei -la para mostrar os detalhes e também os arquivos ocultos. Usei ~ para indicar minha pasta HOME. Por fim, usei > para redirecionar a saída do comando para o arquivo lista_HOME.txt, criando-o caso não exista ou substituindo seu conteúdo caso ele já exista.
ls -la ~ > lista_HOME.txt

# Para mostrar a data atual diretamente na tela, usei o comando date, que exibe a data e o horário atuais do sistema.
date
