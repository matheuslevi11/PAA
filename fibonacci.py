from time import time
import seaborn as sns

def Timer(func, n, nome):
    t1 = time()
    result = func(n)
    t2 = time()
    print(f'{nome} para {n} executou em {(t2-t1)}s')
    return t2-t1

def recursive_fib(n):
    if n <= 1:
        return 1
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)

def iterative_fib(n):
    prev1 = prev2 = 1
    for i in range(2,n):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    return prev1 + prev2

iterative_times = []
recursive_times = []
for i in range(41):
    iterative_times.append(Timer(iterative_fib, i, "Iterativo"))
    recursive_times.append(Timer(recursive_fib, i, "Recursivo"))

sns.lineplot(x=range(41), y=iterative_times)
sns.lineplot(x=range(41), y=recursive_times)
