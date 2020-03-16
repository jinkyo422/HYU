//2015005078_정진교_A
#include <stdio.h>

int temp[100001];
void merge(int* arr, int left, int mid, int right){
    
    int i = left;
    int j = mid+1;
    int k = left;
    int x;
    
    while(i<=mid && j<=right){
        if(arr[i]>=arr[j])
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }

    if(i>mid)
        for(x = j; x<=right; x++)   temp[k++] = arr[x];

    else
        for(x = i; x<=mid; x++)     temp[k++] = arr[x];
    
    for(int x = left; x<=right; x++)    arr[x] = temp[x];

}
void merge_sort(int* arr, int left, int right){
    
    int mid;
    
    if(left<right){
        mid = (left+right)/2;
        merge_sort(arr, left, mid);
        merge_sort(arr, mid+1, right);
        merge(arr, left, mid, right);
    }
}
int main(){
    
    int n;
    int arr[100001];
    
    scanf("%d", &n);
    
    for(int i = 1; i<=n; i++)   scanf("%d", arr+i);
    
    merge_sort(arr, 1, n);
    
    for(int i = 1; i<=n; i++)   printf("%d\n", arr[i]);
    
    return 0;
}
