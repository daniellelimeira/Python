# Escreva um programa que leia três números. O programa deverá retornar uma lista com os valores em ordem.

lista = []
continuar = 'S'

while continuar != 'N':
    numero = int(input('Digite um número inteiro: '))
    lista.append(numero)
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
#    validacao = False
#    while validacao != True:
#        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
#        if continuar == 'SN':
#           validacao = True
#        else:
#            print('A opção não é válida, digite novamente.')
lista.sort()
print(lista)
# OU
# print(sorted(lista))


