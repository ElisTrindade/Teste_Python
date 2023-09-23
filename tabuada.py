#Tabuada

tabuada = int(input("Qual tabuada deverá ser impressa? (1 a 10)"))

for numero in range (0, 11):
    tab = tabuada*numero
    print(f"{tabuada} x {numero}  = {tab}")
