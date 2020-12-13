def factorial(x):

    if x <= 0:
        return x+1
    else:
        return x * factorial(x-1)
result = []
while True:
   try:
      n = input().split()
      a = int(n[0])
      b = int(n[1])
      result.append(factorial(a) + factorial(b))
   except EOFError:
       break

for i in range(0,len(result)):
    print(result[i])
