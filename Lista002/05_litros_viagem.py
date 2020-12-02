#Calcular a quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12km
#com 1 litro. Deverão. Ser fornecidos a) tempo gasto na viagem; b) e a velocidade media. Apresentar os
#valores da velocidade media, tempo gasto, distancia percorrida e quatidade de litros gastos.

print("Informe o tempo gasto em horas:")
tempo_gasto_h = float(input())

print("Informe a velocidade media (km/h):")
velocidade_media_km_h = float(input())

distancia_km = velocidade_media_km_h * tempo_gasto_h

litros = distancia_km / 12

print("velocidade media:", velocidade_media_km_h)
print("tempo gasto:", tempo_gasto_h)
print("distancia percorrida:", round(distancia_km, 2))
print("litros gastos:", round(litros, 2))