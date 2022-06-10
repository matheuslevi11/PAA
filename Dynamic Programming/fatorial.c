#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long int fatorial(int n)
{
    long long int fat[n+1];
    for (int i = 0; i < 3; i++)
    {
        fat[i] = i;
    }
    for (int i = 3; i <= n; i++)
    {
        fat[i] = i * fat[i-1];
    }
    return fat[n];
}

int main()
{
    char string[16];
    while(1)
    {
        scanf("%s", string);
        if (!strcmp(string, "0")) return 0;
        printf("%lli\n", fatorial(strlen(string)));
    }
    return 0;
}