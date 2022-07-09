def prog1(k, c):
    if k == 1:
        print("Oi")
        c += 1
        return c
    else:
        for i in range(1,k+1):
            print("Oi")
            c += 1
        return prog1(k-1, c)

def cont(n):
    c = 0
    for l in range(1, n+1):
        for i in range(1, n-l+1):
            for k in range(1, i+l+1):
                c += 1
    return c

def asterisco(n):
    if n > 0:
        asterisco(n-1)
        for i in range(n):
            print('*', end='')
        asterisco(n-1)

def recorrencia_asterisco(n):
    if n == 1:
        return 1
    return 2 * recorrencia_asterisco(n-1) + n

def recorrencia(n):
    if n == 1: return 1
    return recorrencia(n-1) + n

def f(n):
    return (n * (n-1))/2 + n

for i in range(1, 6):
    print(recorrencia(i))
    print(f(i))