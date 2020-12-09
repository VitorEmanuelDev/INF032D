#5. Dado uma lista de números, faça com que os números sejam ordenados e, em seguida, inverta a
#ordem da lista usando slicing.

numeros = [5, 6, 4, 7, 8, 9, 1, 2, 3, 0]

sorted_numeros = sorted(numeros)
print(sorted_numeros)

reverse_numeros = sorted_numeros[::-1]
print(reverse_numeros)
