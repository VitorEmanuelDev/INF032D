#4. Calcular o salario liquido de um professor. Os dados fornecidos serão: a) valor hora aula; b) numero de
#aulas dadas; c) percentual de desconto INSS.

print("Informe o valor da hora-aula:")
hora_aula = float(input())

print("Quantas aulas ocorreram?")
num_aulas = int(input())

print("Quanto de INSS?")
inss = float(input())

inss = ((inss / 100) - 1) * -1

salario_liquido = (hora_aula * num_aulas) * inss

print("salario liquido: R$",round(salario_liquido, 2))