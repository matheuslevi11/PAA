"""
algoritmo(A[])
    ordena(A) # Ordena a lista em ordem crescente de fi
    S = []
    tempo = 1
    for i de 0 até n:
        if A[i].si >= tempo:
            S += A[i]
            tempo = A[i].fi + 1
    return S
"""
def algoritmo(entrada):
    # Ordena a entrada pelo fi
    S = []
    tempo = 1
    for i in range(len(entrada)):
        if entrada[i]['si'] >= tempo:
            S.append(entrada[i])
            tempo = entrada[i]['fi']+1
    return S

entrada = []
entrada.append({'si': 1, 'fi': 3}) 
entrada.append({'si': 5, 'fi': 6})
entrada.append({'si': 7, 'fi': 8})
entrada.append({'si': 4, 'fi': 10})

print(algoritmo(entrada))