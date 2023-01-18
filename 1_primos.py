def primo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def nPrimeirosPrimos(n):
    primos = []
    x = 2
    while x <= n:
        if primo(x):
            primos.append(x)
        x = x + 1
    return primos

primos = nPrimeirosPrimos(5)
print(primos)