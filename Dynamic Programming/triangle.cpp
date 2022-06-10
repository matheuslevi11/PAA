#include <bits/stdc++.h>

using namespace std;

int minSumPath(vector<vector<int>>& Triangle, int n)
{
    int dp[n][n];
    // Inicializa o caso base
    for (int i = 0; i < n; i++)
    {
        dp[n-1][i] = Triangle[n-1][i];
    }
    // Calcula os subproblema
    for (int i = n-2; i >= 0; i--)
    {
        for (int j = 0; j < i+1; j++)
        {
            dp[i][j] = Triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1]);
        }
    }
    return dp[0][0];
}

/* Driver program to test above functions */
int main()
{
    vector<vector<int> > A{ { 2 },   
                            { 5, 4 },
                            { 3, 4, 7 },
                            { 1, 6, 9, 6 } };
    cout << minSumPath(A, A.size()) << endl;
    return 0;
}