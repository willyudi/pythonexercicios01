#!/usr/bin/env python
# encoding: utf-8
mercadoria = float(input ('Digite o valor da mercadoria: R$ '))
percentual = float(input ('Digite o percentual de desconto: '))
valordesconto = (mercadoria * percentual ) / 100
preco = mercadoria - valordesconto
print ('Valor do desconto: R$ %.2f ' % valordesconto)
print ('Preço a pagar: R$ %.2f ' % preco)
