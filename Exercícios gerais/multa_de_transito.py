# Escreva um programa que pergunte a velocidade de um mototrista. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo
# que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km/h acima de 80 km/h

limite = 80
multa = 5
velocidade = int(input('Qual é a velocidade do carro? '))
excedente = velocidade - limite
if velocidade > limite:
    print(f'Você ultrapassou o limite de velocidade permitido em {excedente} km/h.\n'
          f'MULTA: R${excedente * multa}')
else:
    print(f'Você está dentro do lmite de velocidade, vá em paz!')
