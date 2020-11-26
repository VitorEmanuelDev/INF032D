import math

volume_pote = 15 * 10 * 13
volume_bolinha = 4/3 * (math.pi * 1.2 ** 3)

contador = math.ceil((volume_pote * 0.74) // volume_bolinha)

#volumes_bolinhas = 0
#contador = 0
#fracao = 0

#while fracao <= 0.74:
#    volumes_bolinhas += volume_bolinha
#    fracao = volumes_bolinhas / volume_pote
#    contador += 1

print('Cabem {} bolinhas no pote de Krissia.'.format(contador))

