v = 0
t = 0
aux = []

deslocamento = []
while True:
    try:
        aux = input().split()
        calculo = (int(aux[1]) * 2) * int(aux[0])
        deslocamento.append(calculo)
    except EOFError:
        break


for i in range(0,len(deslocamento)):
    print(deslocamento[i])
