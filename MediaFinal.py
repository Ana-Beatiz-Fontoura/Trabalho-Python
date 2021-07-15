p1 = float(input('Digite a nota da P1: '))

p2 = float(input('Digite a nota da P2: '))

media1 = (p1 + p2)/2

if p1 < 0 or p1 > 10:
    print('Nota inválida!')

elif p2 < 0 or p2 > 10:
    print('Nota inválida!')

elif media1 >= 7:
    print('Aprovado direto! Sua média final é:',media1)

elif media1 < 3:
    print('Reprovado direto! Sua média é:', media1)

else:
    print('Você está de prova final')

    pf = float(input('Coloque a nota da prova final: '))

media_final = (media1 + pf)/2

if media_final >= 5:
    print('Aprovado! Sua média é:', media_final)

else:
    print('Reprovado! Sua média é:', media_final)