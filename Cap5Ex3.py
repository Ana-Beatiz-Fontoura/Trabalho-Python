'''Escreva um programa que leia uma string do teclado e informe se a mesma
é um palíndromo. Assuma que a string lida nunca conterá caracteres
alfabéticos acentuados.'''

texto = str(input('Entre com o texto sem acentos: '))

junto = ''.join(texto).upper()

inverso = ''

for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]

if inverso == junto:
    print('É um palíndromo!')

else:
    print('Não é um palíndromo!')



