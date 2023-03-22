#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários
# superiores a R$1.250,00, calcule um aumento de 10%. Para salários inferiores ou iguais, o aumento será de 15%.

salario = float(input('Salário: R$ '))
if salario > 1250:
    novo_salario = salario + (salario * 0.10)
    print(f'Seu aumento foi de R${salario * 0.10}\nNovo Salário: R${novo_salario}')
else:
    novo_salario = salario + (salario * 0.15)
    print(f'Seu aumento foi de R${salario * 0.15}\nNovo Salário: R${novo_salario}')