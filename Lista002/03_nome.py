#3. Entrar com um nome e imprimir: a) todo o nome; b) primeiro carcater; c) ultimo carcater; d) do primeiro
#ate o terceiro caracter; e)quarto caracter; f) os dois últimos.

print("Escreva um nome:")
nome = input()

nome_char_0 = nome[0]
nome_char_ultimo = nome[-1]
nome_char_0_a_2 = nome[0:3]
nome_char_3 = nome[3]
nome_char_dois_ultimos = nome[-2:]

print("nome completo:", nome)
print("primeira letra:", nome_char_0)
print("ultima letra", nome_char_ultimo)
print("tres primeiras letras:", nome_char_0_a_2)
print("quarta letra:", nome_char_3)
print("duas ultimas letras", nome_char_dois_ultimos)