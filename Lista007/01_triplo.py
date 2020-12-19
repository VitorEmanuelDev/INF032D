# 1. Entrar como n's números e imprimir o triplo de cada. o programa encerra quando
# entrar com o numero 999;

n = int(input("Informe uma quantidade de números que gostaria determinar:"))

lista = []

for i in range(0, n):
    lista[i] = int(input())

for i in range(0, n):
    print(lista[i] * 3)
    resposta = input("Deseja continuar?")
    if resposta == "999"
    exit