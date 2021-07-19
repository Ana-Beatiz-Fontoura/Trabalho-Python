'''Faça um programa que leia uma string do teclado e imprima essa mesma
string com os caracteres alfabéticos com caixa invertida, isto é, os caracteres maiúsculos devem ser impressos minúsculos e os maiúsculos devem
ser impressos minúsculos'''

texto = input('Entre com o texto: ')

novo_texto = ''

for c in texto:
    if 'a'<= c <= 'z':
        carac = c.upper()

    else:
        carac = c.lower()
    novo_texto += carac

print('O novo texto é:', novo_texto)