//2015005078_정진교_A
#include <stdio.h>

int arr[100001];
void swap(int a, int b){
    
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}
void heapify(int i, int n){
    
    int index = i, max = arr[i];
    
    if(i*2 <= n && max < arr[i*2]){
        max = arr[i*2];
        index = i*2;
    }
    if(i*2 + 1 <= n && max < arr[i*2 + 1]){
        max = arr[i*2 + 1];
        index = i*2 + 1;
    }
    if(index != i){
        arr[index] = arr[i];
        arr[i] = max;
        heapify(index, n);
    }
}
void bulidmaxheap(int n){
    for(int i = n/2; i>0; i--)  heapify(i, n);
}
void heapsort(int n, int k){
    
    bulidmaxheap(n);
    int count = 0;
    
    for(int i = n; i>1; i--){
        if(count == k)  break;
        count++;
        swap(1, i);
        n--;
        
        heapify(1, n);
    }
    
}
int main(){

    int n, k;
    
    scanf("%d %d", &n, &k);
    
    for(int i = 1; i<=n; i++)   scanf("%d", arr + i);
    
    heapsort(n, k);
    
    for(int i = n; i>n-k; i--)  printf("%d ", arr[i]);
    printf("\n");
    
    for(int i = 1; i<=n-k; i++) printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}

