#Ler o ano de nascimento da pessoa
ano_nascimento = int(input("Digite o ano de nascimento: "))

#Calcular o ano atual
import datetime
ano_atual = datetime.datetime.now().year

#Calcular a idade da pessoa
idade = ano_atual - ano_nascimento

#Verificar se a pessoa pode votar este ano
if idade >= 16:
    print("Você pode votar este ano!")
else:
    print("Você não pode votar este ano.")
