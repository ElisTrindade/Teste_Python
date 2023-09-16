
# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).

nota = float(input("Insira uma nota de 0 a 100 "))

if (nota >= 90 and nota <= 100):
    print(f"Seu conceito é: A")
elif (nota >= 80 and nota <= 89):
    print(f"Seu conceito é: B")
elif (nota >= 70 and nota <= 79):
    print(f"Seu conceito é: C")
elif (nota >= 60 and nota <= 69):
    print(f"Seu conceito é: D")
elif (nota < 60):
    print(f"Seu conceito é: F")
else:
    print(f"Erro: sua nota máxima é 100")