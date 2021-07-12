hora_partida = input('Entre com o horário de partida: ')
hora_partida = int(hora_partida)

minuto_partida = input('Entre com o minuto da partida: ')
minuto_partida = int(minuto_partida)

hora_chegada = input("Entre com a hora de chegada: ")
hora_chegada = int(hora_chegada)

minuto_chegada = input('Entre com o minuto da chegada: ')
minuto_chegada = int(minuto_chegada)

print('O trem partiu as',hora_partida,':',minuto_partida,'e chegou as',hora_chegada,':',minuto_chegada)

tempo_partida_em_minutos = (hora_partida * 60) + minuto_partida

tempo_chegada_em_minutos = (hora_chegada * 60) + minuto_chegada

tempo_total_viagem = tempo_chegada_em_minutos - tempo_partida_em_minutos


print('O tempo total de viagem foi de:',tempo_total_viagem,'minutos')
