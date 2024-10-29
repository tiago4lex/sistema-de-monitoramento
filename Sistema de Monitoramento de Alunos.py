import json

arquivo_alunos = 'alunos.json'

def salvar_dados():
    with open(arquivo_alunos, 'w', encoding='utf-8') as arquivo:
        json.dump(alunos, arquivo, indent=4)
    
    print('Dados salvos com sucesso!')
    
def carregar_dados():
    try:
        with open(arquivo_alunos, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return{}
    except json.JSONDecodeError:
        print('Erro ao ler o arquivo')
        return{}
    
alunos = carregar_dados()

def cadastrar_aluno():
    while True:
        nome_aluno = input('\nDigite o nome do Aluno: ')
        matricula = input('Digite a matricula do Aluno: ')
        
        if matricula in alunos:
            print('Matricula ja cadastrada')
            continue
        
        num_disciplinas = int(input('Digite o numero de disciplinas cursadas: '))
        disciplinas = []
        
        for i in range(num_disciplinas):
            disciplina = {}
            disciplina_nome = input(f'\nDigite o nome da disciplina {i+1}: ')
            num_avaliacoes = int(input(f'Digite o numero de avaliacoes da disciplina {i+1}: '))
            max_faltas = int(input(f'Digite a quantidade máxima de faltas da disciplina {i+1}: '))
            
            notas = []
            for j in range(num_avaliacoes):
                while True:
                    try:
                        nota = float(input(f'\nDigite a nota {j+1} (de 0 a 10) da disciplina {i+1}: '))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        
                        else:
                            print('Nota inválida. A nota deve estar entre 0 e 10.')
                    except ValueError:  
                        print('Entrada inválida. Por favor, digite um número.')
                        
            while True:
                try:
                    faltas = int(input(f'\nDigite o número de faltas da disciplina {i+1}: '))
                    if faltas >= 0:
                        break
                    
                    else:
                        print('Quantidade de faltas inválida. A quantidade de faltas deve ser maior ou igual a zero.')
                except ValueError:
                    print('Entrada inválida. Por favor, digite um número.')
                    
            disciplina['nome'] = disciplina_nome
            disciplina['notas'] = notas
            disciplina['faltas'] = faltas
            disciplina['max_faltas'] = max_faltas
            disciplinas.append(disciplina)
            
        alunos[matricula] = {
            'nome': nome_aluno,
            'disciplinas': disciplinas
        }
        
        salvar_dados()
        
        print(f"\nAluno {nome_aluno} cadastrado com sucesso!")
        break
    
def gerar_relatorio_aluno(matricula):
    info_aluno = alunos[matricula]
    print(f"\nRelatório do aluno: {info_aluno['nome']}")
    print(f"Matrícula: {matricula}")
    reprovacoes = 0

    for disciplina in info_aluno['disciplinas']:
        media = sum(disciplina['notas']) / len(disciplina['notas'])
        reprovado_por_falta = disciplina['faltas'] > disciplina['max_faltas']
        reprovado_por_nota = media < 6.0

        status = "Aprovado"
        if reprovado_por_falta:
            status = "Reprovado por faltas"
            reprovacoes += 1
        elif reprovado_por_nota:
            status = "Reprovado por nota"
            reprovacoes += 1

        print(f"\nDisciplina: {disciplina['nome']}")
        print(f"Notas: {disciplina['notas']}")
        print(f"Média final: {media:.2f}")
        print(f"Faltas: {disciplina['faltas']} (máximo permitido: {disciplina['max_faltas']})")
        print(f"Status: {status}")

    print(f"\nTotal de disciplinas reprovadas: {reprovacoes}")

def listar_alunos_alfabeticamente():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return None

    lista_ordenada = sorted(alunos.items(), key=lambda item: item[1]['nome'])

    print("\nAlunos cadastrados (em ordem alfabética):")
    for i, (matricula, info_aluno) in enumerate(lista_ordenada, 1):
        print(f"{i}. {info_aluno['nome']} (Matrícula: {matricula})")

    while True:
        try:
            opcao = int(input("\nDigite o número do aluno para gerar o relatório: "))
            if 1 <= opcao <= len(lista_ordenada):
                matricula_selecionada = lista_ordenada[opcao - 1][0]
                return matricula_selecionada
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Digite um número válido.")

def calcular_media_e_aprovacao():
    matricula_selecionada = listar_alunos_alfabeticamente()
    
    if matricula_selecionada:
        gerar_relatorio_aluno(matricula_selecionada)        

def menu():
    while True:
        print("\n1. Cadastrar Aluno")
        print("2. Gerar Relatório Final")
        print("3. Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            if alunos:
                calcular_media_e_aprovacao()
            else:
                print("Nenhum aluno cadastrado.")
        elif opcao == "3":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()