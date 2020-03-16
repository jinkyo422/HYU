//2015005078_정진교_A
#include <stdio.h>

int arr[30001];
int main(){
    
    int n, m, min, index;
    
    scanf("%d %d", &n, &m);
    
    for(int i = 1; i<=n; i++)   scanf("%d", arr + i);
    
    for(int i = 1; i<=m; i++){
        min = arr[i];
        index = i;
        for(int j = i; j<=n; j++){
            if(min > arr[j]){
                min = arr[j];
                index = j;
            }
        }
        if(arr[i] > min){
            arr[index] = arr[i];
            arr[i] = min;
        }
    }
    
    for(int i = 1; i<=n; i++)   printf("%d\n", arr[i]);
    
    return 0;
}

