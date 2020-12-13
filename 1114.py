senha_Correta = int(2002)
senha = 0
count = 0
while senha != senha_Correta:

    senha = int(input())
    count +=1

for i in range(1,count):
    print("Senha Invalida")

print("Acesso Permitido")
