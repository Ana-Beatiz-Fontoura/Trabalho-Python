mes = int(input('Digite o número do mês: '))
mes31 = [1,3,5,7,8,10,12]

if mes < 1:
    print("Mês inválido!")

elif mes > 12:
    print("Mês inválido!")

elif mes == 2:
    print('Mês com 28 dias')

elif mes == mes31:
    print('Mês com 31 dias')

else:
    print('Mês com 30 dias')




