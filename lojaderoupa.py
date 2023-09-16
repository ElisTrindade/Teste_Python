print("========================== Loja de Roupas =============================== ")
valor_venda = float(input("Insira o valor da compra "))
tipo_venda = (input("Insira se a compra é a vista ou a prazo (a vista/a prazo) "))

import sys
## Vendas a vista ================================================================ 
if (tipo_venda == "a vista" and valor_venda > 500 and valor_venda <= 1000):
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
    if (parcelamento > 18):
        print("Erro: insira a quantidade de parcela corretamente (Até 18x)")
        sys.exit()
    elif (parcelamento <=10):
        print("Valor total da parcela sem juros")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total)
        print(f"Valor da parcela: {valor_mensal}")
    else:
        if(parcelamento == 11): juros = 5
        elif(parcelamento == 12): juros = 6.5
        elif(parcelamento == 13): juros = 7
        elif(parcelamento == 14): juros = 9
        elif(parcelamento == 15): juros = 9.5
        elif(parcelamento == 16): juros = 10
        elif(parcelamento == 17): juros = 11.3
        elif(parcelamento == 18): juros = 12
        print(f"Valor total acrescido de {juros}% de juros ao mês")
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total + ((juros/100)*parcelamento_total))
        print(f"Valor da parcela: {valor_mensal}")
        print(f"Obrigada pela compra, volte sempre!")
            
elif (tipo_venda == "a prazo" and valor_venda <= 800):
    parcelamento = int(input("Em quantas vezes deseja parcelar? (Até 5x)"))
    if (parcelamento > 5):
        print("Erro: insira a quantidade de parcela corretamente (Até 5x)")
    else:
        parcelamento_total = (valor_venda/parcelamento)
        valor_mensal =(parcelamento_total)
        print(f"Valor da parcela: {valor_mensal}")
        print(f"Obrigada pela compra, volte sempre!")
