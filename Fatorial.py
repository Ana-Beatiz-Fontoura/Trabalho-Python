n = int(input('Entre com o número: '))

resultado = 1
contador = 1

while contador <= n:
    resultado *= contador
    contador += 1

print(resultado)