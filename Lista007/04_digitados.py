#4.Entrar com vários números e informar quantos números entre 100 e 200 foram
#digitados. quando o valor 0 for digitado o programa deve encerrar;

soma = 0
numero = 1

while numero != 0:
    numero = int(input("Informe um número:"))
    if 100 < numero < 200:
        soma += 1
        print("Foram digitados", soma, "números entre 100 e 200")
    elif numero == 0:
        print("Foram digitados",soma,"números entre 100 e 200")
        print("Programa terminado")