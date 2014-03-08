#!/usr/bin/env python
# encoding: utf-8
salario = float(input ('Digite o salário: R$ '))
percentual = float(input ('Digite o percentual de aumento: '))
valoraumento = (salario * percentual ) / 100
novosalario = valoraumento + salario
print ('Valor do aumento: R$ %.2f ' % valoraumento)
print ('Valor do novo salário: R$ %.2f ' % novosalario)
