# Crie um programa que leia nome, sexo e idade de vários pessoas, guardando os
# dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas; B) A média de idade
# do grupo; C) Um lista com todas as mulheres; D) Uma lista com todas as pessoas
# com idade acima da média.

# ler nome, sexo e idade, colocando em um dicionário e este em uma lista:
pessoas = list()
dados = dict()
soma = 0
media = 0

while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Por favor, digite S ou N.')
    if continuar == 'N':
        break

# Mostrar total de cadastros:
print()
print('-' * 35)
print(f'Foram cadastradas {len(pessoas)} pessoas.')

# Calcular a média de idade dos cadastros:
media = soma / len(pessoas)
print(f'A média de idades eh {media:5.2f} anos')
print('-' * 35)

# Lista com todas as mulheres:
print('As mulheres cadastradas foram:')
for i in pessoas:
    if i['sexo'] == 'F':
        print(f'    * {i["nome"]}')

# Lista de todas as pessoas com idade acima da média:
print('As pessoas com idade acima da média são:')
for i in pessoas:
    if i['idade'] > media:
        print(f'    * {i["nome"]}')