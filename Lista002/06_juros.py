#6. Entrar com valor de um empréstimo, a taxa de juros e a quantidade de meses. Fazer um programa que
#calcule o valor da prestação.

print("Qual o valor do empréstimo?")
emprestimo = float(input())

print("Qual o valor da taxa?")
taxa = (float(input()) / 100) + 1

print("Qual a quantidade de meses?")
meses = int(input())

parcela = (taxa * emprestimo) / meses

print("O valr da parcela é de: R$", round(parcela, 2))