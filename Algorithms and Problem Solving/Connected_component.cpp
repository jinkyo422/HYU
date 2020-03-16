//2015005078_정진교_A
#include<stdio.h>
#include<iostream>

using namespace std;

int arr[1001];
int n;
int visit[1001];
int find(int a){
    
    if (arr[a] != a) {
        arr[a] = find(arr[a]);
    }
    return arr[a];
}
void uni(int a, int b){
    arr[find(b)] = find(a);
}
int main(){
    
    int a, b, count = 0;
    
    scanf("%d", &n);
    
    for(int i = 1; i<=n; i++)   arr[i] = i;
    
    while(scanf("%d %d", &a, &b) != EOF){
        uni(a,b);
    }
    
    for(int i = 1; i<=n; i++){
        find(i);
    }
    
    for(int i = 1; i<=n; i++){
        if(visit[arr[i]] == 0){
            visit[arr[i]] = ++count;
        }
    }
    
    printf("%d\n", count);
    
    for(int i = 1; i<=n; i++){
        printf("%d\n", visit[arr[i]]);
    }
    
    return 0;
}
