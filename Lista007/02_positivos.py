#2.Entrar com números enquanto forem positivos, e imprimir quantos números foram
#digitados;

i = 0
n = 1
while n >= 0:
    n = int(input("Informe um número:"))
    i += 1
    if n < 0:
        i -= 1
        print("Form digitados:", i,"números")
        exit
