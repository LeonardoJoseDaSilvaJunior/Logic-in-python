print("[E] Etanol R$ 4,90L\n[G] Gasolina R$ 5,80L")
tipo_Combustivel = input("Insira o tipo de combustivel: ")
gasolina = 4.80
etanol   = 4.90
litros = float(input("insira a quantidade de litros de Combustivel: "))
if tipo_Combustivel in "Gg":
    total = litros * gasolina
    print(f"----- CONTA -----\nLitros de gasolina: {litros:.1f}L\nValor total: {total:.2f}")
elif  tipo_Combustivel in "Ee":
    total = litros * etanol
    print(f"----- CONTA -----\nlitros de etanol : {litros:.1f}L\nValor total: {total:.2f}")
else:
    print("insira um combustivel valido")



