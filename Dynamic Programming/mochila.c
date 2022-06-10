#include <stdio.h>
#include <stdlib.h>

typedef struct Object object;

struct Object {
    int value;
    int weight;
};

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

int mochila(object objects[], int n, int W)
{
    int dp[n+1][W+1];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= W; j++)
        {
            dp[i][j] = -1;
        }
    }
    // Inicializa primeira linha e primeira coluna como 0
    for (int i = 0; i <= n; i++)
    {
        dp[i][0] = 0;
    }
    for (int i = 0; i < W+1; i++)
    {
        dp[0][i] = 0;
    }
    // Calcula os subproblemas
    for (int j = 1; j < W+1; j++)
    {
        for (int i = 1; i <= n; i++)
        {
            int w = objects[i-1].weight;
            int v = objects[i-1].value;
            if (w > j)
            {
                dp[i][j] = dp[i-1][j];
            }
            else {
                int choose = dp[i-1][j-w] + v;
                int dontChoose = dp[i-1][j];
                dp[i][j] = max(choose, dontChoose);
            }
        }
    }
    //print_matrix(n+1, W+1, dp);
    return dp[n][W];
}

int main()
{
    int tests;
    scanf("%d", &tests);
    for (int i = 0; i < tests; i++)
    {
        int n, g, x;
        scanf("%d", &n);
        object objects[n];
        for (int j = 0; j < n; j++)
        {
            scanf("%d %d", &objects[j].value, & objects[j].weight);
        }
        scanf("%d", &g);
        int W = 0;
        for (int j = 0; j < g; j++)
        {
            scanf("%d", &x);
            W += x;
        }
        printf("%d\n", mochila(objects, n, W));
    }
    return 0;
}