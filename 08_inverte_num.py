original = 123
numero = original
contador = 0

#while numero != 0:
#    numero //= 10
#    contador += 1

#zeros = 10 ** (contador - 1)
#novo = 0
#numero = original

#for i in range(contador):
#    temp = numero % 10
#    novo += int(temp * zeros)
#    zeros /= 10
#    numero //= 10

#print(novo)

novo = 0

temp = numero % 10
novo += int(temp * 100)
numero //= 10

temp = numero % 10
novo += int(temp * 10)
numero //= 10

temp = numero % 10
novo += int(temp)
numero //= 10

print(novo)