num = int(input("Digite um numero maior ou igual a 2: "))

primos = []
x = 2

for n in range(2, num+1):
    primo = 1
    for i in range(2, n):
        if (n % i == 0):
            primo = 0
    if (primo == 1):
        primos.append(n)
    else:
        pass

print(primos)