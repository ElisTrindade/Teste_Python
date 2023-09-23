# Laço de repetição 
# ============================== Imprima números ===============================

num_max = int(input("Insira um número máximo para impressão"))
num_order = input("O número deve ser impresso em ordem crescente ou decrescente? (C/D)")

if num_order == 'C':
    for num_max in range (1, num_max+1):
        print(num_max)
elif num_order == 'D':
    for num_max in range (num_max, 0, -1):
        print(num_max)
else:
    print("Ordem inválida!")

