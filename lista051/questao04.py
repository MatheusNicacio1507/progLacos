'''
Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1 + 2 + 3 + 4 + ...
+ 97 + 98 + 99 + 100)
'''

contador = 1
acumulador = 0 #elemento neutro da soma/sub é 0 e o da multi/div é 1

while (contador <= 100):
    acumulador = acumulador + contador
    contador = contador + 1

print(f"A soma dos valores de 1 a 100 é = {acumulador}")