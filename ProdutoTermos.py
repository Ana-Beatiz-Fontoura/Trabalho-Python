
from math import prod

n_termos = int(input('Digite o número de termos que deseja calcular: '))

i = 1
lista = []
while i <= n_termos:
    lista.append(int(input(f'Insira o {i}º número inteiro: ')))
    i += 1

print('O produto é:', prod(lista))