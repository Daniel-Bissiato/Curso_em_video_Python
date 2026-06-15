from formatacoes import *

caixa_simples('EX 04 -- Ler o que foi digitado e exibir seu tipo primitivo e outras informações')


a = input('\nDigite qualquer coisa: ')


linha_grande()


print(f'Você digitou: {a}.')


print(f'\nO tipo primitivo é: {type(a)}')

print(f'\nSó tem espaço: {a.isspace()}')

print(f'\nÉ um número: {a.isnumeric()}')

print(f'\ntem apenas letras: {a.isalpha()}')

print(f'\nEstá tudo em maiúsculo: {a.isupper()}')

print(f'\nEstá tudo em minúsculo: {a.islower()}')

print(f'\nA primeira letra é maiúscula: {a.istitle()}')
