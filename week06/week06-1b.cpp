///�e�P�P, �q9x9���k���}�l
#include <stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){ ///����i
        for(int j=1;j<=n;j++){ ///�k��j
            printf("*");
        }
        printf("i:%d\n", i);
    }
}