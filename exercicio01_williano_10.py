#!/usr/bin/env python
# encoding: utf-8
cigarros = int(input ('Quantidade de cigarros por dia: '))
anos = int(input ('Quantos anos fuma: '))
perda = 10
dias = (cigarros * anos * 365 * perda) / 1440
print ('Você terá %.0f ' % dias + 'dias a menos de vida.')
