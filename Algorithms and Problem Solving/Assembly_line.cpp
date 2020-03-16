//2015005078_정진교_A
#include <stdio.h>

int a[2][101];
int t[2][101];
int s[2][101];
int l[2][101];
int arr[101];
int main(){
    
    int n, e1, e2, x1, x2, i;
    
    scanf("%d %d %d %d %d", &n, &e1, &e2, &x1, &x2);
    
    for(i = 1; i<=n; i++)   scanf("%d", &a[0][i]);
    
    for(i = 1; i<=n; i++)   scanf("%d", &a[1][i]);
    
    for(i = 1; i<=n-1; i++)   scanf("%d", &t[0][i]);
    
    for(i = 1; i<=n-1; i++)   scanf("%d", &t[1][i]);
    
    s[0][1] = e1 + a[0][1];
    s[1][1] = e2 + a[1][1];
    
    for(i = 2; i<=n; i++){
        int min = s[0][i-1] + a[0][i];
        int temp = 1;
        if(min > s[1][i-1] + a[0][i] + t[1][i-1]){
            min = s[1][i-1] + a[0][i] + t[1][i-1];
            temp = 2;
        }
        s[0][i] = min;
        l[0][i] = temp;
        
        min = s[1][i-1] + a[1][i];
        temp = 2;
        if(min > s[0][i-1] + a[1][i] + t[0][i-1]){
            min = s[0][i-1] + a[1][i] + t[0][i-1];
            temp = 1;
        }
        s[1][i] = min;
        l[1][i] = temp;
    }
    
    int result = s[0][n] + x1;
    int index = 1;
    
    if(result > s[1][n] + x2){
        result = s[1][n] + x2;
        index = 2;
    }
    
    arr[n] = index;
    
    for(i = n-1; i>0; i--)
        arr[i] = l[arr[i+1]-1][i+1];
    
    printf("%d\n", result);
    
    for(i = 1; i<=n; i++)   printf("%d %d\n", arr[i], i);
    
    return 0;
}

