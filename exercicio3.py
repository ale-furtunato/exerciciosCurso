primeiro_valor = int(input("Digite um valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor '{primeiro_valor}' e maior que o segundo valor '{segundo_valor}'")
elif primeiro_valor == segundo_valor:
    print(f"Ambos os valores sao iguais '{primeiro_valor} e {segundo_valor}'")
elif primeiro_valor < segundo_valor:
    print(f"O segundo valor '{segundo_valor}' e maior que o primeiro valor '{primeiro_valor}'")
else:
    print('Error!')