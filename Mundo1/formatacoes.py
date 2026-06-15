# título
def caixa_simples(texto):
    print(f"""┌{"─" * 100}┐
│{texto.center(100)}│
└{"─" * 100}┘""")


# linha
def linha_grande():
    print(f'{"━" * 140 }')
