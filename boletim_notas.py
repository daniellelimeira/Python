# Boletim de notas

alunos = list()

# Ler o nome e duas notas de vários alunos
print('------ SISTEMA DE NOTAS ------\nA seguir insira o nome e as duas notas do aluno')
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1º Nota: '))
    nota2 = float(input('2º Nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media]) # Guardar tudo em uma lista composta
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('*' * 25)
# Mostar boletim contendo media de cada um e permitir que usuario possa mostrar as notas de cada aluno individualmente
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' * 25)

opcao1 = str(input('Deseja ver notas individuais de algum aluno? [S/N] '))
if opcao1 in 'Ss':
    while True:
        opcao2 = int(input('Mostrar notas de qual aluno? '))
        if opcao2 <= len(alunos) - 1:
            print('-' * 40)
            print(f'{alunos[opcao2][0]} | 1º Nota: {alunos[opcao2][1][0]} | 2º Nota: {alunos[opcao2][1][1]}')
            print('-' * 40)
            opcao3 = str(input('Deseja sair? [S/N] '))
            if opcao3 in 'Ss':
                break
        else:
            print('Aluno não cadastrado, por favor inserir novo número')
print('\n*** VOCÊ SAIU DO SISTEMA DE NOTAS ***')



