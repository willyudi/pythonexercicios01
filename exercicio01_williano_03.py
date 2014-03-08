#!/usr/bin/env python
# encoding: utf-8
dia = int(input ('Dias: '))
hora = int(input ('Horas: '))
minuto = int(input ('Minutos: '))
segundos = int(input ('Segundos: '))
totalseg = (dia * 86400) + (hora * 3600) + (minuto * 60) + segundos
print ('O total em segundos é: ' + str(totalseg) + 's')