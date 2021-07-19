'''Faça um programa que leia uma string do teclado e informe a quantidade
de caracteres alfabéticos maiúsculos na string.'''

texto = input('Entre com o texto: ')

maiusculo = 0

for c in texto:
    if c.isupper():
        maiusculo += 1

print('O número de caracteres alfabéticos maiúsculos é:',maiusculo)
