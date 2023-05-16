from library.functions import *
while True:
    n = int(input("insira um número "))
    primo(n)
    validacao =int(input("Deseja continuar? digite 1: "))
    if validacao == 1:
        break