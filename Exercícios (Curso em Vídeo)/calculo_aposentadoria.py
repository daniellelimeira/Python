# Criar um programa que leia nome, ano de nascimento e carteira de trabalho. Cadastre-os (com idade) em um dicionário,
# se a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, o ano de aposentadoria. Considerar a aposentadoria depois de 35 anos de colaboração.

from datetime import datetime

ficha = dict()
ficha['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
ficha['Idade'] = datetime.now().year - nascimento
ficha['CTPS'] = int(input('Nº da carteira de trabalho (0 se não possui): '))
if ficha['CTPS'] != 0:
    ficha['Ano de contratação'] = int(input('Ano de contratação: '))
    ficha['Salário'] = float(input('Salário: R$ '))
    ficha['Idade de posentadoria'] = ficha['Idade'] + ((ficha['Ano de contratação'] + 35) - datetime.now().year)
print('-' * 40)
for k, v in ficha.items():
    print(f'{k} é igual a {v}')