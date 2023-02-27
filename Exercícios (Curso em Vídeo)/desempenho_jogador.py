# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
# vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o
# campeonato.

# Criar dic. para informaçõe do jogador e lista para armazenar os gols por partida
ficha = dict()  # ficha do jogador
aproveitamento = list()  # nº de gols/partida

ficha['nome'] = str(input('Nome do jogador: '))  # armazenar nome no dic.

# Armazenar nº de gols considerando o nº de partidas
c = 0
partidas = int(input('Número de partidas jogadas: '))
while c < partidas:
    aproveitamento.append(int(input(f'Quantos gols fez na partida {c}? ')))
    c += 1

# Armazenar o aproveitamento (nº de gols/partida) e o total de gols
ficha['gols'] = aproveitamento[:]
ficha['total'] = sum(aproveitamento)

# Exibir dicionário
print('*' * 45)
print(ficha)
print('*' * 45)

# Exibir as chaves e respectivos valores do dicionário
for k, v in ficha.items():
    print(f'O campo {k} tem valor {v}.')
print('*' * 45)

# Exibir informações do jogador acessando informações da lista dentro do dicionário
print(f'O jogador {ficha["nome"]} jogou {len(ficha["gols"])} partidas.')
for i, v in enumerate(ficha['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Fez um total de {ficha["total"]} gols.')
