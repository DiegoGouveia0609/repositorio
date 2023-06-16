# Ler os três valores inteiros
valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

# Verificar e escrever os valores em ordem crescente
if valor1 < valor2 and valor1 < valor3:
    menor = valor1
    if valor2 < valor3:
        meio = valor2
        maior = valor3
    else:
        meio = valor3
        maior = valor2
elif valor2 < valor1 and valor2 < valor3:
    menor = valor2
    if valor1 < valor3:
        meio = valor1
        maior = valor3
    else:
        meio = valor3
        maior = valor1
else:
    menor = valor3
    if valor1 < valor2:
        meio = valor1
        maior = valor2
    else:
        meio = valor2
        maior = valor1

# Imprimir os valores em ordem crescente
print("Valores em ordem crescente: {}, {}, {}".format(menor, meio, maior))
