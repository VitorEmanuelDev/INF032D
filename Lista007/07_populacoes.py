#7.Dado um pais A, com 5.000.0000 de habitantes e uma taxa de natalidade de 3% ao
#ano, e um pais B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano.
#calcular e imprimir o tempo necessário para que a população do pais A ultrapasse a
#população do pais B;

pais_A = 5000000
natalidade_A = 1.03
pais_B = 70000000
natalidade_B = 1.02

i = 0

while pais_A < pais_B:
    pais_A *= natalidade_A
    pais_A *= natalidade_A
    i += 1
    if pais_A > pais_B:
        print("Serão necessários",i,"anos para o país A superar o país B em população.")