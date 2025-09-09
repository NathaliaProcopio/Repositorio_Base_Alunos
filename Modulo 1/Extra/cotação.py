
COTACAO_DOLAR = 5
def real_dolar(reais):
    return reais / COTACAO_DOLAR

def dolar_real(dolares):
    return dolares * COTACAO_DOLAR

opcao = input("Selecione a opção que deseja:\n" \
"[1 -> Converter de real para dólar]: \n" \

"[2 -> Converter de dólar para real]:\n ")

if opcao == "1":
    real = float(input("Digite o valor que quer converter.\n"))
    print(f"Você tem: USD${real_dolar(real)}")
elif opcao == "2":
    dóllar = float(input("Digite o valor que quer converter.\n"))
    print(f"Você tem: R${dolar_real(dóllar)}")
else:
    print("Opção inválida.")



