#4. Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!
#Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista.
#Agora «vá à sorveteria» e se empanturre de sorvete e tire o sorvete da lista.

sorvete = ["Morango com Chocolate"]
frutas = ["Banana", "Manga", "Abacaxi", "Siriguela"]
limpeza = ["Agua sanitária", "Sabão", "Detergente"]

mercado = [sorvete, frutas, limpeza]

del mercado[-1]

print(mercado)

del mercado[0]

print(mercado)