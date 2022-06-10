def calculate(l):
    acc = 0
    for i in range(len(l)):
        acc += (i+1) * l[i]
    return acc

print(calculate([2, 4, 1, 3, 5]))