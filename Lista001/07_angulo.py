import math
from math import radians, sin, cos, tan

angulo = 80

seno = (sin(radians(angulo)))
co_seno = (cos(radians(angulo)))
tangente = (tan(radians(angulo)))
secante = 1 / (cos(radians(angulo)))
co_secante = 1 / (sin(radians(angulo)))
co_tangente = (cos(radians(angulo))) / (sin(radians(angulo)))


print('{} seno'.format(round(seno,2)))
print('{} cosseno'.format(round(co_seno, 2)))
print('{} tangente'.format(round(tangente, 2)))
print('{} secante'.format(round(secante,2)))
print('{} co_secante'.format(round(co_secante,2)))
print('{} co_tangente'.format(round(co_tangente,2)))