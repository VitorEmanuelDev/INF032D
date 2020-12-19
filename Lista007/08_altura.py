#8.Chico tem 1.50m e cresce 2 centímetros por ano, enquanto Juca tem 1.10m e cresce 3
#cm por ano. construir um programa que calcule e imprima quantos anos serão necessários
#para Juca seja maior que Chico;

chico = 1.5
crescimento_chico = .02
juca = 1.1
crescimento_juca = .03

i = 0

while chico > juca:
    chico += crescimento_chico
    juca += crescimento_juca
    i += 1
    if juca > chico:
        print("Serão necessários",i,"anos para Juca ser mais alto que Chico.")