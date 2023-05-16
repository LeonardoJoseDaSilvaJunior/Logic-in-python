def count (n):
    for x in range(1,n+1):
        print(x*str(x))
def imprime_nome(nome):
    print(f"hello, my name is {nome}")
def vogais(texto):
    count = 0
    for x in texto:
        if x in "AaEeIiOoUu":
            count += 1
    print(count)
def adicao (n1,n2):
    return n1 + n2
def subtracao (n1,n2):
    return n1 - n2
def divisao (n1,n2):
    return n1 / n2
def multiplicacao (n1,n2):
    return n1 * n2
def positivo_Negativo(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"
list_produto = []
list_preco = []
def produto_Preco (produto,preco):
    list_produto.append(produto)
    list_preco.append(preco)
def infinita(*numero):
   return sum(numero)
#16/5/2023

def inverter_texto(texto):
   print(f"A palavra '{texto}' contém {len(texto)} letras e é escrito ao contrário da seguinte forma '{texto[::-1]}'")

def excluir_duplicados(list):
    existentes = []
    for x in range(len(list)):
        if list[x] not in existentes:
            existentes.append(list[x])
    return existentes
def primo(n):
    if n == 1:
        return n, print("O número {} Não é primo!".format(n))
    elif n ==2:
        return n,"É primo"
    for x in range(2, n):
        if n % x == 0:
            return n,print("O número {} Não é primo!".format(n))
    return print("O número {} é primo!".format(n))



