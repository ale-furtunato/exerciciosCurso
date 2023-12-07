nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso: "))
imc = peso / (altura * altura)

print(f"{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC e {imc}")