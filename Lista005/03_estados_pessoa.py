#3.Entrar com a sigla do estado de uma pessoa, e imprimir se é carioca, Paulista,
#mineira ou outros estados.

print("Informe a sigla do estado de origem de alguém:")
estado = input()
estado = estado.lower()

if estado == 'rj':
    print("Carioca")
elif estado == 'sp':
    print("Paulista")
elif estado == 'mg':
    print("Mineira")
else:
    print("Outros estados")
