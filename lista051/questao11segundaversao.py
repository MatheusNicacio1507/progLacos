'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um expoente qualquer (Variável e), ou seja, de belevado a e. (Sem usar Math.pow();)
'''

b = float(input("Insira um número: "))

e = float(input("Insira um expoente: "))

pot = b ** e

print(f"{b:.0f} elevado à {e:.0f} é = {pot:.0f}")


