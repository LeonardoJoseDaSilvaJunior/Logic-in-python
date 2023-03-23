primeiraNota = float(input("Insira a primeira nota:"))
while primeiraNota < 0:
    print("Nota menor que zero, insira uma nota válid")
    primeiraNota = float(input("Insira a primeira nota:"))
    if(primeiraNota > 0):
        break
segundaNota = float(input("Insira a Segunda nota:"))
while segundaNota < 0:
    print("Nota menor que zero, insira uma nota válid")
    segundaNota = float(input("Insira a segunda nota:"))
    if(segundaNota > 0):
        break

media = (primeiraNota + segundaNota)/2



print("\n__________BOLETIN_________")
print("Primeira nota: {0}\nSegunda nota: {1}\nMedia{2}".format(primeiraNota,segundaNota,media))