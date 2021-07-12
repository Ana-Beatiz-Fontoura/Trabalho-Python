a = complex(input('Coloque o valor de a: '))


b = complex(input('Coloque o valor de b: '))


c = complex(input('coloque o valor de c: '))


delta = b**2 - (4*a*c)
print(delta)

x1 = (-b + (delta ** 0.5))/2*a

x2 = (-b - (delta ** 0.5))/2*a

print(x1)

print(x2)
