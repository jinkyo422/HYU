//2015005078_정진교_A
#include <stdio.h>
#define INF -987654321

int arr[101];
int r[101];
int s[101];
void cut(int n){
    
    for(int i = 1; i<=n; i++){
        int temp = INF;
        for(int j = 1; j<=i; j++){
            if(temp < arr[j] + r[i-j]){
                temp = arr[j] + r[i-j];
                s[i] = j;
            }
        }
        r[i] = temp;
    }
}
void sol(int n){
    while(n>0){
        printf("%d ", s[n]);
        n = n-s[n];
    }
}
int main(){
    
    int n;
    
    scanf("%d", &n);
    
    for(int i = 1; i<=n; i++)   scanf("%d", arr+i);
    
    cut(n);
    
    printf("%d\n", r[n]);
    
    sol(n);
    
    return 0;
}

