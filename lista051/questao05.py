'''
Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser impressa no seguinte formato:

Considerando como exemplo o fornecimento do número 2

2 . 1 = 2
2 . 2 = 4
2 . 3 = 6
2 . 4 = 8
2 . 5 = 10
(...)
2 . 10 = 20
'''

num = int(input("Insira um número: "))

contador = 1

while(contador <= 10):
    print(f"{num}.{contador} = {num * contador}")
    contador = contador + 1
