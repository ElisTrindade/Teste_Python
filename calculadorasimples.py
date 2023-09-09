# Cálculadora simples ================================================

#Peça ao usuário para inserir dois números e uma operação (+, -, *, /).
#Realize a operação e exiba o resultado.

num_1 = float(input("Insira um número "))
num_2 = float(input("Insira mais um número "))
operaçao = (input("Insira uma operação (+, -, *, /)"))

if (operaçao == "+"):
   sum = num_1 + num_2
   print(f"{sum}")
elif (operaçao == "-"):
   sum = num_1 - num_2
   print(f"{sum}")
elif (operaçao == "*"):
   sum = num_1 * num_2
   print(f"{sum}")
elif (operaçao == "/"):
   sum = num_1 / num_2
   print(f"{sum}")
else:
    print(f"erro")