// 백준10991 : 별 찍기 - 16
#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
        for (int j = N-i-1; j > 0; j--)
            printf(" ");
        for (int j = 0; j < i+1; j++)
            printf("* ");
        printf("\n");
    }

    return 0;
}