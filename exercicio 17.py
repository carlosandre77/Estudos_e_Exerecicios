"""faca um programa que leia o comprimento do
cateto oposto e do cateto adjacente de um
triangulo retangulo, calcule e mostre o comprimento da hipotenusa"""
from math import hypot
c_op=(float(input('digite o cateto oposto: ')))
c_ad=(float(input('digite o cateto adjacente: ')))
print( ' a hipotenusa é {} '.format(hypot(c_op,c_ad)**(1/2)))