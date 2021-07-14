Lado1 = float(input('Digite o comprimeto do primeiro lado do triângulo: '))

Lado2 = float(input('Digite o comprimento do segundo lado do triângulo: '))

Lado3 = float(input('Digite o comprimento do terceiro lado do triângulo: '))

if (Lado1 + Lado2 < Lado3) or (Lado3 + Lado1 < Lado2) or (Lado3 + Lado2 < Lado1):
    print('Não é um triângulo!')

elif Lado1 == Lado2 == Lado3:
    print('O triângulo é equilátero!')

elif Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
    print('O triângulo é isósceles!')

else:
    print('O triângulo é escaleno!')

