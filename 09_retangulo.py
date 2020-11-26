import math

Aa = 5
Bb = 10

area = Aa * Bb
perimetro = Aa * 2 + Bb * 2
diagonal = math.sqrt(Aa ** 2 + Bb ** 2)

print('area = {}'.format(round(area, 2)))
print('perimetro = {}'.format(round(perimetro, 2)))
print('diagonal = {}'.format(round(diagonal, 2)))
