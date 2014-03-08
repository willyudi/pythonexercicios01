#!/usr/bin/env python
# encoding: utf-8
distancia = float(input ('Distância em km: '))
velocidade = float(input ('Velocidade em km/h: '))
tempo = distancia / velocidade
print ('O tempo estimado de viagem é: %.2f ' % tempo + 'horas')
