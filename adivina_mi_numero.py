# -*- coding: utf-8 -*-
"""Adivina mi numero.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JD8vFn4PHsQ0FNFXM-qoao15ynugGvNG
"""

from random import random
numero_secreto = int(100*random())
print('Adivina un numero del 0 al 100\n')
# inicia declaración de control iterativo
flag = True # = NO ADIVINÓ. Cuando <<buscamos>> algo podemos usar un flag
i = 0
while flag :
  print('Intento ',i+1)
  numero_ingresado = int(input('Escribe tu numero: '))
  if numero_secreto == numero_ingresado:
    print('Felicitaciones. Adivinaste, el número secreto era',numero_secreto)
    flag = False
    break
  elif numero_secreto < numero_ingresado:
    print('Ingresa un número más pequeño')
  else:
    print('Ingresa un número más grande')
  i = i+1
#fin de control iterativo
print('Has adivinado el número usando', i+1, 'intentos')