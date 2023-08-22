'''
Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar, mostre-o; não sendo, passe para o próximo passo.
'''
#Regra 1 declarar contador da estrutura de repetição
contador = 0

#Regra 2: testar a estrutura (while com var contador) no valor fim da repetição
while(contador <= 20):

    #bloco que será repetido várias vezes
    impar = contador % 2

    if(impar == 1):
        print(f"O número {contador} é ímpar")


    #Regra 3: incrementar a var contador na última linha dentro do bloco
    contador = contador + 1