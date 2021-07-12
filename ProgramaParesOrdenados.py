variavel_x_1 = input('Entre com o valor x no primeiro ponto:')
variavel_x_1 = float(variavel_x_1)

variavel_y_1 = input('Entre com o valor de y no primeiro ponto:')
variavel_y_1 = float(variavel_y_1)

variavel_x_2 = input('Entre com o valor de x no segundo ponto:')
variavel_x_2 = float(variavel_x_2)

variavel_y_2 = input('Entre com o valor de y no segundo ponto:')
variavel_y_2 = float(variavel_y_2)

distancia_pontos = ((variavel_x_2 - variavel_x_1)**2 + (variavel_y_2 - variavel_y_1)**2)**0.5
print(distancia_pontos)

coef_angular = (variavel_y_2 - variavel_y_1)/(variavel_x_2 - variavel_x_1)
print(coef_angular)

coef_linear = variavel_y_1 - (coef_angular*variavel_x_1)
print(coef_linear)

