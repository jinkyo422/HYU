//2015005078_정진교_A
#include <stdio.h>

int a[100001];
int b[100001];
int c[100001];
int main(){
    
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    
    for(int i = 1; i<=k; i++)   scanf("%d %d", a+i, b+i);
    
    for(int i = 1; i<=n; i++){
        int temp;
        scanf("%d", &temp);
        c[temp]++;
    }
    
    for(int i = 1; i<=m; i++)   c[i] = c[i] + c[i-1];
    
    for(int i = 1; i<=k; i++)   printf("%d\n", c[b[i]] - c[a[i] - 1]);
    
    return 0;
}
