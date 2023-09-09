# Cálculadora de juros simples ====================


valor = float(input("Qual o valor principal?"))
taxa = float(input("Qual a taxa de juros anual?"))
taxa = taxa/100
periodo = float(input("Qual o período de tempo em anos?"))

montante = valor + (valor*taxa*periodo)
juros = valor*taxa*periodo

print(f"O valor total anual do juros é: {juros}")
print(f"O valor total anual é: {montante}")

