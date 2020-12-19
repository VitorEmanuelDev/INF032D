#6.Entrar com vários números ate entrar com o numero 999. para cada numero imprimir
#seus divisores;

numero = 0

while numero != 999:
    numero = int(input("Informe um número inteiro:"))
    if numero != 999:
        print("Divisores:")
        i = 1
        while i <= numero:
            if numero % i == 0:
                print(i)
            i += 1
    else:
        print("Tchau!")
