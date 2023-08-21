'''
Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar, mostre-o; não sendo, passe para o próximo passo.
'''

contador = 1

while(contador <= 20):
    impar = contador % 2

    if(impar == 1):
        print(f"O número {contador} é ímpar")

    contador = contador + 1