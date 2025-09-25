def calcular_salario(horas_trabalhadas, valor_hora):
    return horas_trabalhadas * valor_hora

valor_hr = float(input("Digite quanto você ganha por hora? "))
qnt_hr =float(input("Digite quantas horas trabalhou por mês: "))

salario = calcular_salario(qnt_hr, valor_hr)

print(f"{salario:.2f}")


