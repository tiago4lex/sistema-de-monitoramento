# Sistema de Monitoramento de Desempenho Acadêmico

Este projeto é um sistema de controle de desempenho acadêmico desenvolvido para auxiliar uma escola na gestão eficiente da lista de alunos, incluindo o registro de faltas e notas para diversas disciplinas. O sistema permite a geração de um relatório completo da situação de cada aluno.

## Funcionalidades

### 1. Registro de Alunos e Disciplinas
- Permite cadastrar alunos informando nome e número de matrícula (único).
- Solicita ao usuário o número de disciplinas cursadas por cada aluno.
- Para cada disciplina, o usuário pode registrar:
  - Nome da disciplina.
  - Número de avaliações.
  - Quantidade máxima de faltas permitidas.

### 2. Entrada de Notas e Faltas
- Para cada disciplina, o sistema solicita as notas de cada avaliação e o número de faltas do aluno.
- Valida para garantir que o número de faltas não exceda o limite estabelecido para a disciplina.

### 3. Cálculo de Média e Verificação de Aprovação
- O sistema calcula a média de cada disciplina com base nas notas inseridas.
- Verifica se o aluno atingiu a média mínima de 6.0.
- Verifica se o aluno ultrapassou o limite de faltas, resultando em reprovação por falta.

### 4. Relatório Final
- Gera um relatório completo, exibindo:
  - Nome do aluno, número de matrícula, nome das disciplinas, notas, média final e número de faltas.
  - Indica se o aluno foi aprovado ou reprovado em cada disciplina, com base na média e nas faltas.
  - Exibe o número total de disciplinas em que o aluno foi reprovado.

## Validações do Sistema
- O programa valida que o usuário insira notas válidas (entre 0 e 10) e faltas não negativas.
- Garante que os números de matrícula sejam únicos, evitando duplicatas.
- Utiliza laços `for` e `while` para iterar sobre os alunos e disciplinas.
- Armazena os dados em dicionários e listas, utilizando dicionários aninhados para representar cada aluno e suas disciplinas.

## Tecnologias Utilizadas
- Linguagem de Programação: Python
- Estruturas de Dados: Dicionários e listas
- Validação de dados

## Como Executar
1. Clone o repositório para sua máquina local.
2. Execute o script Python diretamente no terminal.
3. Siga as instruções para registrar os alunos, notas e faltas.
4. Gere o relatório final para verificar o desempenho dos alunos.

