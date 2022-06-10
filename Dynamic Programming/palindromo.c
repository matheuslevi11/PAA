#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Object object;

void print_matrix(int n, int m, int matrix[][m])
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d ", matrix[i][j]); 
        }
        printf("\n");
    }
}

int max_palindrome(char word[], int n)
{
    int dp[n][n];
    // Inicializa os casos base
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            dp[i][j] = 0;
        }
    }
    for (int i = 0; i < n; i++)
    {
        dp[i][i] = 1;
    }
    for (int i = 0; i < n-1; i++)
    {
        if (word[i] == word[i+1]) dp[i][i+1] = 1;
        else dp[i][i+1] = 0;
    }
    int answer = 1;
    // Calcula os subproblemas
    for (int k = 2; k < n-1; k++)
    {
        for (int i = 0; i < n-k; i++)
        {
            int j = i+k;
            if (word[i] == word[j] && dp[i+1][j-1]){
                dp[i][j] = 1;
                if (j+1 > answer) answer = j+1;
            } 
            else dp[i][j] = 0;
        }
    }
    if (word[0] == word[n-1] && dp[1][n-2])
    {
        dp[0][n-1] = 1;
        answer = n;
    }
    return answer;
}

int main()
{
    int t;
    scanf("%d", &t);
    char words[t][1000];
    for (int i = 0; i < t; i++)
    {
        scanf("%s", words[i]);
    }
    for (int i = 0; i < t; i++)
    {
        if(words[i][0] != 1)
        {
            printf("%d\n", max_palindrome(words[i], strlen(words[i])));
        }
        else
            printf("0\n");
    }
    return 0;
}