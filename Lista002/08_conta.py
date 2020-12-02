#8. Dado um numero de conta corrente com três dígitos, retorne o seu digito verificador, o qual é calculado da
#seguinte maneira. Exemplo: numero conta 235, somar o numero da conta com seu inverso : 235+532=767.
#Multiplicar cada digito pela sua ordem posicional e somar estes resultados: 7 6 7 (7x1+6x2+7x3) = 40. O
#ultimo digito desse resultado é o digito verificador da conta (40-> 0 )

print("Informe tres digitos:")
digitos = int(input())

numero = digitos

inverso = 0

temp = numero % 10
inverso += int(temp * 100)
numero //= 10

temp = numero % 10
inverso += int(temp * 10)
numero //= 10

temp = numero % 10
inverso += int(temp)
numero //= 10

soma_inverso_digitos = digitos + inverso

terceiro = soma_inverso_digitos % 10
soma_inverso_digitos //= 10
segundo = soma_inverso_digitos % 10
soma_inverso_digitos //= 10
primeiro = soma_inverso_digitos

verificador = (primeiro + segundo * 2 + terceiro * 3) % 10

print("conta: {}-{}".format(digitos,verificador))