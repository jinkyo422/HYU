//2015005078_정진교_A
#include <stdio.h>

int arr[100001];
int first[100001];
void swap(int a, int b){
    
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}
void heapify(int i, int n){
    
    int index = i*2, max = arr[i];
    
    while (index <= n) {
        if (index < n && arr[index] <= arr[index + 1]) {
            index++;
        }
        if (max < arr[index]) {
            arr[index/2] = arr[index];
            index = index * 2;
        }
        else
            break;
    }
    arr[index/2] = max;
}
void insert(int n){
    
    for (int i = n; i/2>=1; i= i/2) {
        if (arr[i] > arr[i/2])  swap(i, i/2);
        else break;
    }
}
int main(){
    
    int command, n = 0, k = 0, flag = 1, temp;
    
    while(flag){
        scanf("%d", &command);
        
        switch (command) {
            case 0:
                for(int i = 1; i<=k; i++)   printf("%d ", first[i]);
                printf("\n");
                for(int i = 1; i<=n; i++)   printf("%d ", arr[i]);
                printf("\n");
                flag = 0;
                break;
                
            case 1:
                n++;
                scanf("%d", arr + n);
                if(n > 1)   insert(n);
                break;
                
            case 2:
                k++;
                first[k] = arr[1];
                arr[1] = arr[n--];
                heapify(1, n);
                break;
                
            case 3:
                int a;
                scanf("%d %d", &a, &temp);
                arr[a] = temp;
                if(a != 1 && arr[a] > arr[a/2])    insert(a);
                else heapify(a, n);
                break;
                
            default:
                break;
        }
    }
    return 0;
}
