///week13-3.cpp ブ猭
#include <stdio.h>
int main()
{
    int n; ///璶р计–秨
    scanf("%d",&n);
    int N=0; ///Τ碭计
    int a[20] = {};
    while(n>0){
        int now = n%10; ///瞷ㄓ计
        printf("now:%d\n",now);
        n = n/10; ///俱计埃猭,琵n跑
    }
    int bad = 0;
    for(int i=0;i<N;i++){
        if(a[i]!=a[N-1-i]) bad=1;
    }
    if(bad==1) printf("NO\n");
    else printf("YES\n");
}
