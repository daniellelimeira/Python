menu = int(input('------\n Menu\n------\n\n1 - Cadastrar data de emprestimo\n0 - Sair da biblioteca\n'))
datas = list()
dia = list()
mes = list()
ano = list()

if menu == 1:
    for c in range(0, 2):
        print('----------------\nNOVO EMPRESTIMO\n----------------')
        dia.insert(c, int(input('Digite o dia do emprestimo: ')))
        mes.insert(c, int(input('Digite o mes do emprestimo: ')))
        ano.insert(c, int(input('Digite o ano do emprestimo: ')))
    datas.insert(0, dia[:])
    datas.insert(1, mes[:])
    datas.insert(2, ano[:])
    print(datas)
else:
    print('Voce saiu da biblioteca!')


