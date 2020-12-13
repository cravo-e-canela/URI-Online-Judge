x = 1
y = 1
result = []
while x != 0 and y != 0:

    n = input().split()
    x = int(n[0])
    y = int(n[1])

    if x > 0 and y > 0:
        result.append("primeiro")
    elif x > 0 and y < 0:
        result.append("quarto")
    if x < 0 and y > 0 :
        result.append("segundo")
    elif x < 0 and y < 0:
        result.append("terceiro")


for i in range(0,len(result)):
    print(result[i])
