
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))


imc = peso / (altura ** 2)


if imc < 18.5:
    print("IMC: {:.2f} - Abaixo do peso".format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print("IMC: {:.2f} - Peso normal".format(imc))
elif imc >= 25.0 and imc <= 29.9:
    print("IMC: {:.2f} - Sobrepeso".format(imc))
else:
    print("IMC: {:.2f} - Obesidade".format(imc))
