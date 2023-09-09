# Calculo do IMC ====
resposta = input("'Olá, vamos calcular seu imc? (S/N)")

print('Para isso você precisará responder algumas perguntas!')
nome = input("Qual seu nome?")
idade = input("Qual sua idade?")
peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))

# IMC = Peso ÷ (Altura × Altura)

imc = peso // (altura*altura)

print(f"Olá {nome};")
print(f"Sua idade é de {idade} anos.")
print(f"Seu IMC é de {imc};")
