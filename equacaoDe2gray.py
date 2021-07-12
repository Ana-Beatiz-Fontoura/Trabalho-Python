a = input('Coloque o valor de a: ')
a = float(a)

b = input('Coloque o valor de b: ')
b = float(b)

c = input('coloque o valor de c: ')
c = float(c)

delta = b**2 - (4*a*c)
print(delta)

x1 = (-b + (delta ** 0.5))/2*a

x2 = (-b - (delta ** 0.5))/2*a

print(x1)

print(x2)
