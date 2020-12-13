def soma_impares(a,b):
    soma = 0
    if(a > b):
        aux = a
        a = b
        b = aux
    for i in range(a+1,b):
        if((i % 2) != 0):
            soma += i
    return soma

n = int(input())
res = []
i = 0
while i < n:
    valor = input().split()
    if valor:
        x = int(valor[0])
        y = int(valor[1])
        res.append( soma_impares(x,y))

    i += 1

for i in res:
    print(i)
