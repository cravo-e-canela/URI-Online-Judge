a =-1
b=-2
msg =[]
while a != b:
    n = input().split()
    a = int(n[0])
    b = int(n[1])
    if a > b:
      msg.append('Decrescente')
    elif b > a:
        msg.append('Crescente')

for i in range(len(msg)):
    print(msg[i])
