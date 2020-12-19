#5.Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro caracter de
#cada nome;
nome = ""

while nome != "FIM":
    nome = input("Qual nome deseja digitar?")
    nome = nome.upper()
    if nome == "FIM":
        print("Tchau!")
    else:
        print("Primeiro caractere:", nome[0])