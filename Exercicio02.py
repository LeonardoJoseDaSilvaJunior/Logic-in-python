n1 = float(input("Primeiro número: "))
n2 = float(input("segundo número: "))

for i in range(0,4):
    match i:
        case 0:

           resultado = n1+n2
           print(f"{n1} + {n2} = {resultado}")

        case 1:
            resultado = n1 - n2
            print(f"{n1} - {n2} = {resultado}")

        case 2:
            resultado = n1 * n2
            print(f"{n1} * {n2} = {resultado}")

        case 3:
            resultado = n1  /n2
            print(f"{n1} / {n2} = {resultado:.2f}")
            print("Resto: ", (n1%n2))

