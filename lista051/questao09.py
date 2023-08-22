'''
Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize um laço que efetue a variação de 2 em 2.
'''

contador = 2

acumulador = 0

while(contador <= 500):
    par = contador%2

    if(par == 0):
        acumulador = acumulador + contador
        contador = contador + 2

print(f" A soma dos números pares é {acumulador}")

