conta_caminhos(grafo G, s, t)
    n = G.size
    ordena(G de t até s)
    dp[n]
    dp[0] = 1 // De t para t existe um único caminho
    
    for i = 1 até n
        percorre as a arestas de i
            // Soma todas os caminhos de i até t.
            dp[i] += dp[a.destino] 

    return dp[n];


caminho_maximo(grafo G, s, t)
    n = G.size
    ordene(de s até t)
    dp[n]
    dp[0] = 0 // Caminho máximo de s até s é 0
    
    for i = 1 até n
        maior = 0
        percorre os j vizinhos de G[i]
            if dp[j] > maior:
                maior = dp[j]
        dp[j] = maior

    return dp[n]

    /*contador = 1
    while(contador < n)
    {
        percorra os i vizinhos de v
            maior = 0
            percorra os j vizinhos de i
                if dp[j] > maior:
                    maior = dp[j]
            dp[i] = maior
            contador++

    }*/


maior_substring(x[], y[], n, m)
    dp[n][m] // Representa a melhor substring com n letras de x e m letras de y
    
    for i = 0 até n
        dp[i][0] = 0
    for j = 0 até m
        dp[0][j] = 0

    for i = 1 até n
        for j = 1 até m
            if (x[i] == y[j])
                dp[i][j] = 1 + dp[i-1][j-1] // Se letras são iguais, adiciona a solução
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) // Melhor resultado entre tirar uma letra de x ou tirar de y

    return dp[n][m]