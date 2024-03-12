# estrutura conditional
''''
number = int(input("Digte um número inteiro: "))
if number > 0:
    print("Seu valor é positivo")
else:
    print("Seu valor é negativo")
'''

#Escreva um programa em python que receba dois numeros inteiros do usuario e realise a somados dois numeros e o resultado apenas se o segundo numero for maior que o primeiro:

# meu exercicio
'''
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("O resultado da soma é:", num1 + num2)
'''
# Se...
# exercicio do professor
'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# estrutura condicional "if" simples 
if n2 > n1:
    print(f"O resultado da soma é:  {(n1 + n2)}")
'''

# Senão...
'''
numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo!")
else:
    print("O número não é positivo!")
'''

# Se...Senão...Se...
'''
numero = int(input("Digite um número:  "))
if numero > 0:
    print("O número é positivo!")
elif numero < 0:
     print("O número é negativo!")
else:
     print("O número é zero!")
'''

#Escreva um programa em python que, receba dois numeros do usuario e se o primeiro numero for maior calcule e mostre o quadrado da soma dos dois numeros, se o segundo numero for o maior calcule e mostre a soma dos quadrados dos numeros, caso sejam iguais mostrar uma mensagem de erro.
     
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = (num1 + num2)
qn1 = num1 * num2
qn2 =  num1 * num2

if num1 > num2:
    print(soma * soma)
elif num2 > num1:
    print(soma * soma)
else: 
    print("Erro, tente novamente...")
