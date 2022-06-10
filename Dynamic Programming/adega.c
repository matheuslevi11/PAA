#include <stdio.h>
#include <stdlib.h>

void print_matrix(int n, int m, int matrix[][m])
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (matrix[i][j] == -1)
            {
                printf("X ");
            }
            else {
                printf("%d ", matrix[i][j]); 
            }
        }
        printf("\n");
    }
}

int max(int a, int b)
{
    if (a > b) return a;
    return b;
}

int adega(int p[], int n)
{
    int dp[n][n];
    // Visualização
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            dp[i][j] = -1;
        }
    }
    // Inicializa os casos base
    int y = n;
    for (int i = 0; i < n; i++)
    {
        dp[i][i] = p[i] * y;
    }
    // Calcula os subproblemas
    for (int k = 1; k < n; k++)
    {
        y--;
        for (int i = 0; i < n-k; i++)
        {
            int j = i+k;
            int sell_left = dp[i+1][j] + y*p[i];
            int sell_right = dp[i][j-1] + y*p[j];
            dp[i][j] = max(sell_left, sell_right);
        }
    }

    return dp[0][n-1];
}

int main()
{
    int n;
    while (scanf("%d", &n) != EOF)
    {
        int p[n];
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &p[i]);
        }
        printf("%d\n", adega(p,n));
    }
    return 0;
}