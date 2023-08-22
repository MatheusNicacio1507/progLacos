'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um expoente qualquer (Variável e), ou seja, de belevado a e. (Sem usar Math.pow();)
'''

b = float(input("Insira um número: "))

e = float(input("Insira um expoente: "))

#Usuário -> b = 3, e = 4
#No papel -> 3 * 3 * 3 * 3

contador = 1 #Começa valendo no valor que o enunciado sugere
acumulador = 1 # '''''''''''''''' 1 ou 0

while(contador <= e):
    acumulador = acumulador * b
    contador = contador + 1

print(f"{b:.0f} elevado à {e:.0f} é = {acumulador:.0f}")


