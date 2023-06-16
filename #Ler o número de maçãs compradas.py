#Ler o número de maçãs compradas
quantidade_macas = int(input("Digite o número de maçãs compradas: "))

#Verificar o preço por unidade e calcular o valor total da compra
if quantidade_macas < 12:
    preco_por_unidade = 0.30
else:
    preco_por_unidade = 0.25

valor_total = quantidade_macas * preco_por_unidade

#Imprimir o valor total da compra
print("O valor total da compra é R$ {:.2f}".format(valor_total))
