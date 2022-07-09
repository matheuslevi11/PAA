def kth(a1, a2, n, m, k):
    if n == 0:
        return a2[k-1]
    if m == 0:
        return a1[k-1]

    mid1 = (n - 1)//2
    mid2 = (m - 1)//2
    # Se o tamanho dos arrays combinados for menor que k
    print(f"Kc = {mid1+mid2+1}  k = {k}")
    if mid1+mid2+1 < k:
        if a1[mid1] < a2[mid2]:
            print(f"Cortando a primeira metade de a1 {a1} -> {a1[mid1 + 1:]}")
            print(f"k agora é {k-mid1-1}")
            return kth( a1[mid1 + 1:], a2, 
            n - mid1 - 1, m, 
            k - mid1 - 1)
        else:
            print(f"Cortando a primeira metade de a2 {a2} -> {a2[mid2 + 1:]}")
            print(f"k agora é {k-mid2-1}")
            return kth(a1, a2[mid2 + 1:], 
            n, m - mid2 - 1, 
            k - mid2 - 1)
    else:
        if a1[mid1] < a2[mid2]:
            print(f"Cortando a segunda metade de a2 {a2} -> {a2[:mid2 + 1]}")
            if m == 1 and mid2+1 == 1:
                return kth(a1[:mid1+1], a2, n, 0, k)
            return kth(a1, a2[:mid2 + 1], 
            n, mid2 + 1,
            k)
        else:
            print(f"Cortando a segunda metade de a1 {a1} -> {a1[:mid1 + 1]}")
            if n == 1 and mid1+1 == 1:
                return kth(a1[:mid1+1], a2, 0, m, k)
            return kth(a1[:mid1 + 1], a2, 
            mid1 + 1, m, 
            k)

def montanha(A, inicio, fim):
    if inicio == fim - 1:
        return max(A[inicio], A[fim])

    mid = (inicio + fim) // 2

    if A[mid] < A[mid+1]:
        return montanha(A, mid, fim)
    return montanha(A, inicio, mid)

def indice(a, inicio, fim):
    if inicio > fim:
        return -1
    i = (inicio+fim) // 2
    if a[i] > i:
        return indice(a, inicio, i-1)
    elif a[i] < i:
        return indice(a, i+1, fim)
    return i

def stocks(arr):
    if len(arr) <= 1:
        return 0

    left  = arr[ : len(arr) // 2]
    right = arr[len(arr) // 2 : ]

    leftBest  = stocks(left)
    rightBest = stocks(right)

    crossBest = max(right) - min(left)

    return max(leftBest, rightBest, crossBest)
"""
coleta_lucro(A[n])
    if n <= 1:
        return 0

    esquerda = A[0...n/2]
    direita = A[n/2...n]
    melhorEsquerda = coleta_lucro(esquerda)
    melhorDireita = coleta_lucro(direita)
    lucroCruzado = -min(esquerda) + max(direita)
    return max(melhorEsquerda, melhorDireita, lucroCruzado)
"""
def sortTimes(A, placar, inicio, fim):
    if len(A) == 1:
        return [A[0]]
    if len(A) == 2:
        if placar[1][0] == 1:
            print(f"Time {A[0]} venceu de {A[1]}")
            return [A[0], A[1]]
        print(f"Time {A[1]} venceu de {A[0]}")
        return [A[1], A[0]]
    
    mid = (inicio+fim) // 2
    left = A[:mid]
    right = A[mid:fim+1]
    print(f"left {left} right {right}")
    left = sortTimes(left, placar, 0, len(left)-1)
    right = sortTimes(right, placar, 0, len(right)-1)

    return left + right
# inputs
array = [-4, 1, 3, 4, 5]
times = ['paiN', 'INTZ', 'LOUD']
placar = [[-1, 1, 0], [0, -1, 0], [1, 1, -1]]

print(f"Times ordenados: {sortTimes(times, placar, 0, len(times)-1)}")
print(f"O cume da montanha é {indice(array, 0, len(array)-1)}")
"""
kth(a1, a2, n, m, k):
    if n == 0:
        return a2[k-1]
    if m == 0:
        return a1[k-1]

    mid1 = n/2
    mid2 = m/2
    kc = mid1+mid2+1
    if kc < k:
        if a1[mid1] < a2[mid2]:
            return kth(a1[mid1+1...n], a2, n-mid1-1, m, k - mid1 - 1)
        else:
            return kth(a1, a2[mid2+1...m], n, m-mid2-1, k - mid2 - 1)
    else:
        if a1[mid1] < a2[mid2]:
            return kth(a1, a2[0...mid2+1], n, mid2+1, k)
        else:
            return kth(a1[0...mid1+1], a2, mid1+1, m, k)
"""
"""
panqueca(A[n])
    i = n
    while i > 1
        maior_panqueca = max(A[i])
        espatula(maior_panqueca)
        espatula(i-1)
        i--
"""