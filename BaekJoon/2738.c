// 백준2738 : 행렬 덧셈
#include <stdio.h>

int main(void)
{
    int A[100][100];
    int B[100][100];
    int N, M;
    scanf("%d %d", &N, &M);

    int tmp = 1;
    for (int i=0;i<2;i++)
    {
        for (int j=0;j<N;j++)
        {
            if (tmp)
            {
                for (int k=0;k<M;k++)
                    scanf("%d", &A[j][k]);
            }
            else
            {
                for (int k=0;k<M;k++)
                    scanf("%d", &B[j][k]);
            }
        }
        tmp = 0;
    }

    for (int i=0;i<N;i++)
    {
        for (int j=0;j<M;j++)
        {
            A[i][j] += B[i][j];
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }

    return 0;
}