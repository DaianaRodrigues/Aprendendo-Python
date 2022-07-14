qta = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma =  soma + valor
    qta = qta + 1

    #entrada de valores
    valor = float(input("Digite um valor: "))

# caso digite um valor negativo o laço encerra
media = soma / qta
print("\n Total da soma: ", soma)
print("\n Quantidade de valores digitados: ", qta)
print("\n Média dos valores: ", media)

