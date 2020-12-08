#10. Dada a frase “Python é muito legal". use fatiamento para dar nome às variáveis contendo cada palavra.
#Qual o tamanho dessa frase? E qual o tamanho de cada palavra?

frase = "Python é muito legal"

python = frase[0:6]
eh = frase[7]
muito = frase[8:14]
legal = frase[-5:]


print("Tamanho da frase é:", len(frase))
print("Tamanho da de python é:", len(python))
print("Tamanho da eh é:", len(eh))
print("Tamanho da muito é:", len(muito))
print("Tamanho da legal é:", len(legal))