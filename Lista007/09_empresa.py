#9.Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores de
#consumo. para cada consumidor, são digitados os seguintes dados: a)Numero do
#consumidor; b)Quantidade de kWh consumidos durante o mês; c) tipo do consumidor ->
#1-residencial, preço em reias de kWh = 0,3 / 2-comercial, preço em reias de kWh = 0,5 /
#3-industrial, preço em reias de kWh = 0,7. Os dados devem ser lidos ate que seja
#encontrado um consumidor com numero 0(zero). calcular e imprimir: a) o custo total para
#cada consumidor; b)o total de consumo para os 3(três) tipos de consumidor; c)a media de
#consumo dos tipos 1 e 2.

custo = []
kWh_consumidor = []
numero_consumidor = []
tipo_consumidor = []

cons_01 = 0
cons_02 = 0
cons_03 = 0

num_cons = 1
i = 0

while num_cons != 0:

    num_cons = int(input("Qual o número do consumidor?"))
    if num_cons == 0:
        exit
    else:
        if num_cons < 0:
            num_cons *= -1
        numero_consumidor.append(num_cons)

        kWh_cons = float(input("Quantos kWh foram consumidos?"))
        if kWh_cons < 0:
            kWh_cons *= -1
        kWh_consumidor.append(kWh_cons)

        print("1 - Residencial\n2 - Comercial\n3 - Industrial")
        tipo_cons = int(input("Qual o tipo de consumidor?"))
        if tipo_cons != 1 and tipo_cons != 2 and tipo_cons != 3 and tipo_cons != 0:
            print("Escolha apenas uma das opções abaixo:")
            print("1 - Residencial\n2 - Comercial\n3 - Industrial")
            tipo_cons = int(input("Qual o tipo de consumidor?"))
            if tipo_cons != 1 and tipo_cons != 2 and tipo_cons != 3 and tipo_cons != 0:
                tipo_cons = 1
                print("Tipo inválido. Atribuindo tipo 1.")
        tipo_consumidor.append(tipo_cons)

        if tipo_cons == 1:
            custo.append(kWh_cons * .3)
            cons_01 += 1
        elif tipo_cons == 2:
            custo.append(kWh_cons * .5)
            cons_02 += 1
        elif tipo_cons == 3:
            custo.append(kWh_cons * .7)
            cons_03 += 1

        i += 1

if (num_cons == 0 and i == 0) or num_cons == 0:
    print("Programa terminado.")
    exit
else:
    n = i
    custo_total = sum(kWh_consumidor)

    i = 0
    soma_kWh = 0

    while i < n:
        if tipo_consumidor[i] == 1 or tipo_consumidor[i] == 2:
            soma_kWh += kWh_consumidor[i]
        i += 1

    media_01_02 = soma_kWh / (cons_01 + cons_02)

    i = 0

    while i < n:
        print("\nNúmeros dos clientes:", numero_consumidor)
        print("Consumo por cliente (kWh):", kWh_consumidor)
        print("Tipo de cliente:", tipo_consumidor)
        print("Preço/Custo total por consumidor (R$):", custo)

        i += 1

    print("Consumo total (todos os tipos) (R$):", custo_total)
    print("Média de consumo (tipos 01 e 02) (kWh):", media_01_02)