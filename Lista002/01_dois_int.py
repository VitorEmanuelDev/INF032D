#1. Entrar com dois números inteiros e imprimir a seguinte saída: a)dividendo; b) divisor; c) quociente; d) resto.

print("Informe dois números inteiros")
dividendo = int(input())
divisor = int(input())

quociente = dividendo / divisor
resto = dividendo % divisor

print("Dividendo:", dividendo)
print("Divisor", divisor)
print("Quociente", quociente)
print("Resto", resto)