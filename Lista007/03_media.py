#3.Entrar com vários números positivos e imprimir a media dos números digitados. o
#programa acaba quando se informar que não deseja mais continuar.

resposta = "sim"
soma = 0
divisor = 0

while resposta == "sim":
    numero = float(input("Informe um número positivo:"))
    if numero > 0:
        soma += numero
    else:
        numero = numero * -1
        soma += numero
    divisor += 1
    media = soma / divisor
    print("Média atual:", round(media, 2))
    resposta = input("Deseja continuar?")
    resposta = resposta.lower()