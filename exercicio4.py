nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome != '' and idade != '':
    print(f"Seu nome e {nome}")
    print(f"Seu nome invertido e {nome[::-1]}")
    print(f"Seu nome contem {nome!r}")
else:
    print("Desculpe, voce deixou campos vazios.")
