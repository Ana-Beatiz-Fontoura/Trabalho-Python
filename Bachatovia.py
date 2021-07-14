renda = float(input('Digite sua renda anual: '))

variavel1 = (15*renda)/100

variavel2 = 3117.50 + ((28*renda)/100)

variavel3 = 11743.00 + ((31*renda)/100)

if renda < 0:
    print('Renda inválida!')

elif renda <= 21450.00:
    print('Imposto:',variavel1)

elif renda > 21450.00 or renda <= 51900.00:
    print('Imposto:',variavel2)

else:
    print(variavel3)
