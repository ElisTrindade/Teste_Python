
#Peça ao usuário para inserir seu salário e o tempo de serviço. Se o tempo de serviço
#for superior a 5 anos, conceda um bônus de 5% ao salário.

salario = float(input("Insira seu salário "))
tempo_servico = float(input("Insira seu tempo de serviço em anos"))

if (tempo_servico > 5):
    salario_bonificado = salario + (salario*0.05)
    print(f"{salario_bonificado}")
else:
    print(f"{salario}")
