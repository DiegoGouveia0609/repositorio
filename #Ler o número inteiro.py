 #Ler o número inteiro
numero = int(input("Digite um número inteiro entre 1 e 7: "))

# Verificar o número e imprimir o nome do dia da semana correspondente
if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Número inválido")