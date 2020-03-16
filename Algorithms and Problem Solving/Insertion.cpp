//2015005078_정진교_A
#include <stdio.h>

int arr[30001];
int n;
int main(){
    
    scanf("%d", &n);
    
    for(int i = 1; i<=n; i++){
        scanf("%d", arr+i);
    }
    
    for(int j = 2; j<=n; j++){
        int key = arr[j];
        int i = j-1;
        while(i>0 && arr[i]<key){
            arr[i+1] = arr[i];
            i--;
        }
        arr[i+1] = key;
    }
    
    for(int i = 1; i<=n; i++){
        printf("%d\n", arr[i]);
    }
    
    return 0;
}
