nome    = input("Insira seu nome: ")
idade   = int(input("Insira sua idade: "))
salario = float(input("Digite seu salário: "))
percentual = float(input("Insira o seu percentual de aumento: "))
aumento = (percentual/100) * salario
salario_Atual = salario + aumento

print("\n-------------PERFIL DO FUNCINARIO-------------\n\n")
print("Nome:{0}\nIdade: {1} anos\nSalarioc: R$ {2:.2f}.\nPercentual de aumento: {3:.2f}%\nAumento: {4}\nSalario atual: {5:.2f} ".format(nome,idade,salario,percentual,aumento,salario_Atual))
