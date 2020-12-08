#10. Dada a frase “Python é muito legal". use fatiamento para dar nome às variáveis contendo cada palavra.
#Qual o tamanho dessa frase? E qual o tamanho de cada palavra?

frase = "Python é muito legal"

python = frase[0:6]
eh = frase[7]
muito = frase[9:14]
legal = frase[-5:]


print("Tamanho da frase é:", len(frase))
print("Tamanho de de", python, "é:", len(python))
print("Tamanho de'", eh, "'é:", len(eh))
print("Tamanho de'", muito, "'é:", len(muito))
print("Tamanho de'", legal, "'é:", len(legal))