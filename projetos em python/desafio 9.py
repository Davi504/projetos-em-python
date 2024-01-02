#esse programa lê altura e largura de uma parede para sabermos quantos L de tinta vamos precisar considerando 1L = 2m(2)
v1 = float(input('digite a largura da parede:'))
v2 = float(input('digite a altura da parede'))
v3 = v1 * v2 
v4 = v3 / 2
print ('você tem uma parede de {} de área e precisará de {:.2f}L de tinta para pintar a parede'.format(v3, v4))
