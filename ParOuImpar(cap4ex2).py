while True:
    numero = int(input('Entre com um número: '))

    if numero < 0:
       print('Entrada inválida!')

    elif numero%2 == 0:
       print('Esse número é par!')


    else:
       print('Esse número é ímpar!')
       break

x = int(input('Deseja executar o programa novamente? (Sim - 1) ou (Não - 0): '))

if x == 1:
    while True:
        numero = int(input('Entre com um número: '))

        if numero < 0:
            print('Entrada inválida!')

        elif numero % 2 == 0:
            print('Esse número é par!')


        else:
            print('Esse número é ímpar!')
            break
        break
else:
    print('Tenha um bom dia!')