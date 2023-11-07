"""
Desenvolver um programa que calcule o fatorial do número 5, ou seja, 5!. Desta forma, temos que 5! = 5 . 4 . 3 .
2 . 1 ou 5! = 1 . 2 . 3 . 4 . 5, equivalente a 120.
"""

contador = 1
num = 5

while(num > 0):
    contador = contador * num
    num = num - 1

print(f"O fatorial de 5! é = {contador}")

