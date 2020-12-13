i = 0
t = int(input())
casos = []
while(i < t):
    c = float(input())
    casos.append(c)
    i +=1


for i in range(0,len(casos)):
    n = casos[i]
    d = 0.0
    while n > 1.00:
        n /= 2
        d +=1

    print(int(d),"dias")
