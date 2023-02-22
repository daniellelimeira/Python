escolha_menu = int(input('Menu:\nEscolha uma das opções:\n1 - Digitar a data de emprestimo\n0 - Sair da biblioteca\n'))
contador = 0
datas = []
dia = []
mes = []
ano = []

if escolha_menu == 1:
    for contador in range(0, 2):
        print('----------------\nNOVO EMPRESTIMO\n----------------')
        dia.insert(contador, int(input('Digite o dia do emprestimo: ')))
        mes.insert(contador, int(input("Digite o mes do emprestimo: ")))
        ano.insert(contador, int(input("Digite o ano do emprestimo: ")))
    datas.insert(1, dia)
    datas.insert(2, mes)
    datas.insert(3, ano)
    print(datas)
else:
    print('Você saiu da biblioteca com sucesso!')

for i in range(0, 2):
    print(f'Data {i + 1}: {dia[i]}/{mes[i]}/{ano[1]}')
