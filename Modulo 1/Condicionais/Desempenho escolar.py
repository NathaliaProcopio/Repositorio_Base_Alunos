print("------------------------------------------------")
print("SISTEMA DE AVALIAÇÃO DE DESEMPENHO ESCOLAR")
print("------------------------------------------------")


nome = input("Digite o seu nome: ")

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(media)

if media >= 7:
    print("Aprovado")
elif media > 4:
    print("Em Recuperação")
else:
    print("Reprovado")








