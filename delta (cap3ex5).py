a = float(input('Digite o valor de a: '))

b = float(input('Digite o valor de b: '))

c = float(input('Digite o valor de c: '))

delta = b**2 - (4*a*c)

x1 = (-b + (delta ** 0.5))/2*a

x2 = (-b - (delta ** 0.5))/2*a


if a == b == c == 0:
    print('Equação inválida')

elif delta == 0:
    print('A raíz é:',x2)

elif delta > 0:
    print('As raízes são:',x1,'e',x2)

else:
    print('Essa equação não possui raízes reais')


