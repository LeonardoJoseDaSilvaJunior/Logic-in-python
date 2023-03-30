time1 = input("Insira o nome do primeiro time: ")
gols_time1 = int(input("Quantos gols o primeiro time marcou?"))
time2 = input("Insira o nome do segundo time:  ")
gols_time2 = int(input("Quantos gols o segundo time marcou?"))
if(gols_time1>gols_time2):
      print(f"------- RESULTADO -------\n   {time1} {gols_time1} x {time2} {gols_time2}\nO time vencedor foi: {time1}")
else: print(f"------- RESULTADO -------\n {time2} {gols_time2} x {time1} {gols_time1}\nO time vencedor foi: {time2}") if gols_time2 > gols_time1 else print("EMPATE")

