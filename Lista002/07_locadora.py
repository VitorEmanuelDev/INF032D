#7. Criar um programa que leia a quantidade de fitas de uma locadora de vídeo possui e o valor que ela cobra
#por cada aluguel, mostrando as informações pedidas a seguir: a) sabendo que um terço das fitas são
#alugadas por mês, exiba o faturamento anual da locadora; b)Quando o cliente atrasa a entrega, é cobrada
#uma multa de 10% sobre o valor do aluguel. Sabendo que um decimo das fitas alugadas no mês são
#devolvidas com atraso, calcule o valor ganho com multas por mês; c) sabendo ainda que 2% de fitas se
#estragam ao longo do ano, e um decimo do total é comprado para reposição, exiba a quantidade de fitas
#que a locadora terá no final do ano.

print("Quantas fitas a locadora tem?")
fitas = int(input())

print("Qual o valor do aluguel?")
aluguel = float(input())

faturamento_anual = ((fitas * aluguel) / 3) * 12

faturamento_multa = (fitas * (aluguel * .10) / 10) * 12

fitas_final_ano = int((fitas * 1.1) - (fitas * .02))

print("faturamento anual: R$", faturamento_anual)
print("ganhos com multa: R$", faturamento_multa)
print("quantidade de fitas ao final do ano:", fitas_final_ano)