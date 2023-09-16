print("========================== Loja de Roupas =============================== ")

valor_venda = float(input("Insira o valor da venda "))
tipo_venda = (input("Insira se a venda é a vista ou a prazo (a vista/a prazo)"))

## Vendas a vista ================================================================ 

if (tipo_venda == "a vista" and valor_venda > 500):
    print("Você terá 15% de desconto")
    valor_final = (valor_venda - (valor_venda)*(15/100))
    print(f"Valor final será: {valor_final}")
elif (tipo_venda == "a vista" and valor_venda > 1000):
    print("Você terá 20% de desconto")
    valor_final = (valor_venda - (valor_venda)*(20/100))
    print(f"Valor final será: {valor_final}")
elif (tipo_venda == "a vista" and valor_venda <= 500):
    print("Você terá 10% de desconto")
    valor_final = (valor_venda - (valor_venda)*(10/100))
    print(f"Valor final será: {valor_final}")

## Vendas a prazo ===============================================================

if (tipo_venda == "a prazo" and valor_venda > 800):
    parcelamento = int(input("Em quantas vezes deseja parcelar? (Até 18x)"))
    if (parcelamento <=10):
        print("Valor total da parcela sem juros")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total)
        print(f"Valor da parcela: {valor_mensal}")
    if(parcelamento == 11):
        print("Valor total acrescido de 5% de juros ao mês")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total + ((5/100)*parcelamento_total))
        print(f"Valor da parcela: {valor_mensal}")
    elif(parcelamento == 12):
        print("Valor total acrescido de 6.5% de juros ao mês")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total + ((6.5/100)*parcelamento_total))
        print(f"Valor da parcela: {valor_mensal}")
    elif(parcelamento == 13):
        print("Valor total acrescido de 7% de juros ao mês")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total + ((7/100)*parcelamento_total))
        print(f"Valor da parcela: {valor_mensal}")
    elif(parcelamento == 14):
        print("Valor total acrescido de 9% de juros ao mês")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total + ((9/100)*parcelamento_total))
        print(f"Valor da parcela: {valor_mensal}")
    elif(parcelamento == 15):
        print("Valor total acrescido de 9.5% de juros ao mês")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total + ((9.5/100)*parcelamento_total))
        print(f"Valor da parcela: {valor_mensal}")
    elif(parcelamento == 16):
        print("Valor total acrescido de 10% de juros ao mês")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total + ((10/100)*parcelamento_total))
        print(f"Valor da parcela: {valor_mensal}")
    elif(parcelamento == 17):
        print("Valor total acrescido de 11.3% de juros ao mês")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total + ((11.3/100)*parcelamento_total))
        print(f"Valor da parcela: {valor_mensal}")
    elif(parcelamento == 18):
        print("Valor total acrescido de 12% de juros ao mês")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total + ((12/100)*parcelamento_total))
        print(f"Valor da parcela: {valor_mensal}")
if (tipo_venda == "a prazo" and valor_venda <= 800):
    parcelamento = float(input("Em quantas vezes deseja parcelar? (Até 5x)"))
    parcelamento_total = (valor_venda/parcelamento)
    valor_mensal =(parcelamento_total)
    print(f"Valor da parcela: {valor_mensal}")
else:
    print("Informações não reconhecidas, siga as instruções corretamente")

print("Obrigada pela compra, volte sempre!")