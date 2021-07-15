x = float(input('Digite a coordenada x do centro do círculo: '))

y = float(input('Digite a coordenada y do centro do círculo: '))

raio = float(input('Digite o raio do círculo: '))

x_teste = float(input('Digite a coordenada x do ponto de teste: '))

y_teste = float(input('Digite a coordenada y do ponto de teste: '))

distancia = float(((x_teste - x)**2 + (y_teste - y)**2)**0.5)

if distancia < raio:
    print('O ponto está dentro do círculo')

elif distancia == raio:
    print('O ponto está na circunferência (fronteira)')

elif distancia > raio:
    print('O ponto está fora do círculo')

else:
    print('O ponto está no centro do círculo')

