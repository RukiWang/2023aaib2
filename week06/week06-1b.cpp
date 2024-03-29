///畫星星, 從9x9乘法表開始
#include <stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){ ///左手i
        for(int j=1;j<=n;j++){ ///右手j
            printf("*");
        }
        printf("i:%d\n", i);
    }
}
