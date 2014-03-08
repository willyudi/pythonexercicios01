#!/usr/bin/env python
# encoding: utf-8
km = float(input ('Km percorridos: '))
dias = int(input ('Dias de aluguel: '))
diaria = 60
kmrodado = 0.15
preco = (km * kmrodado) + (dias * diaria)
print ('O preço a pagar é: R$ %.2f ' % preco)
