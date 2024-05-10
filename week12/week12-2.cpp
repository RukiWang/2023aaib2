#include <stdio.h>
int main()
{
    int n = 2;
    int a[2][3] = { {10,20,30}, {11,22,33} };
    int b[2][3] = { {3,2,1}, {4,3,2} };
    int c[2][2];
    ///上週教的 part 1 讀資料。先設好 就不用再讀了
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            int * p1 = & a[i][j];
            printf("%3d ",a[i][j]);
        }
        printf("\n");
    }
}
