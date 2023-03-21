# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

nome = str(input('Digite seu nome: ')).upper()
i = 0
while i <= len(nome):
    print(f'{nome[i]}')
    i+= 1