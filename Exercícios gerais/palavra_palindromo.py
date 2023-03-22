# Crie um programa em Python que, dada uma string, informe se ela é um palíndromo ou não. Um palíndromo é
# uma palavra ou frase que é lida da mesma forma da esquerda para a direita e da direita para a esquerda.
# Dica: Se s é uma string, lista ou tupla, então você poderá reverter utilizando passando o valor -1 como
# o terceiro índixe de indexação, ou seja, s[::-1] irá fornecer a a mesma estrutura, com os elementos em ordem reversa.

palavra = str(input('Digite uma palavra: ')).upper()
palavra_invertida = palavra[::-1]
if palavra == palavra_invertida:
    print(f'O inverso de {palavra} é {palavra_invertida}, logo é um palíndromo')
else:
    print(f'O inverso de {palavra} é {palavra_invertida}, logo não é um palíndromo')