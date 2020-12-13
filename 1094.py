n = int(input())
quantia = []
coelhos = 0
ratos = 0
sapos = 0
cobaias = 0
def percentual(c, a):
    p = float(a*100.00) / c
    p = round(p,2)
    return p

for i in range(0,n):
    quantia = input().split()
    if 'C' in quantia:
        coelhos += int(quantia[0])
    elif 'R' in quantia:
        ratos += int(quantia[0])
    elif 'S' in quantia:
        sapos += int(quantia[0])

cobaias = coelhos + sapos + ratos

print('Total: {} cobaias' .format(cobaias))
print('Total de coelhos: {}' .format(coelhos))
print('Total de ratos: {}' .format(ratos))
print('Total de sapos: {}' .format(sapos))
print('Percentual de coelhos: {:05.2f} %' .format(percentual(cobaias,coelhos)))
print('Percentual de ratos: {:05.2f} %' .format(percentual(cobaias,ratos)))
print('Percentual de sapos: {:05.2f} %' .format(percentual(cobaias,sapos)))
