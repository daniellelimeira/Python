# Tamanho de strings. Faça um programa que leia 2 strings e informe o 
# conteúdo delas seguido do seu comprimento. Informe também se as duas 
# strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

print('Compara dua strings')
str_1 = str(input('String 1: '))
str_2 = str(input('String 2: '))
print(f'Tamanho de {str_1}: {len(str_1)} caracteres')
print(f'Tamanho de {str_2}: {len(str_2)} caracteres')
if(len(str_1) != len(str_2)):
    print('As duas strings são de tamanhos diferentes.')
else:
    print('As duas strings possuem o mesmo tamanho.')
  
if(str_1 != str_2):
    print('As duas strings possuem conteúdos diferentes.')
else:
    print('As duas strings possuem o mesmo conteúdo.')