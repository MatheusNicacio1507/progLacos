"""
Desenvolver um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é
formada pela sequência 1,1,2,3,5,8,13,21,34, ... etc. Ela se caracteriza pela soma de um termo posterior com seu
anterior subsequente.
"""

contador = 1
num2 = 1
num = 1

print(num)

while (contador <= 15):
    print(num2)
    soma = num + num2
    num = num2
    num2 = soma
    contador = contador + 1


