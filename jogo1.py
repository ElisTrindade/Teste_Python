# Jogo de adivinhar valores 


from random import randint

numero = randint(0,100)
print(numero)

tentativa = int(input("Chute um valor de 0 a 100"))
contador = 0
while numero != tentativa:
    if (tentativa < numero):
        print(f"{tentativa} é menor que o número")
        tentativa = int(input("Chute um novo valor de 0 a 100"))
        contador = contador+1
    elif (tentativa > numero and tentativa < 100):
        print(f"{tentativa} é maior que o número")
        tentativa = int(input("Chute um novo valor de 0 a 100"))
        contador = contador+1
    else:
        (tentativa > 100)
        print("Número Invalido")
        contador = contador+1

if (tentativa == numero):
        print('Parabéns, voce acertou!')
        print(f'Suas tentativas foram: {contador}')
