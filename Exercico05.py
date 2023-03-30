total = 0
for i in range (0,3):
    nota = float(input("Insira a nota: "))
    total += nota
media = total/3
if   media >= 7: print('Aprovado')
elif media >= 4: print("Recuperacao")
else:            print('reprovado')
