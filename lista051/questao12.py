'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem como maior, nem como menor, e nem na contagem da média.
'''

num = int(input("Insira um número: "))

while (contador != -1):
    num = int(input("Insira outro número: "))

    maior = contador

    if (maior < num2):
        maior = num2

    if (maior < num3):
        maior = num3

    print(f"O maior valor inserido foi {maior}")
    print(f"O menor valor inserido foi {menor}")
