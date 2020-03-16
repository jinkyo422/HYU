//2015005078_정진교_A
#include<stdio.h>
#include<iostream>

using namespace std;

int graph[1001][1001];
int print[1001];
int visit[1001];
int n, t;
int a=1;
int flag = 1;
void dfs(int now) {
    
    visit[now] = 1;
    
    for (int i = 1; i <= n; i++) {
        int next = i;
        if (graph[now][next] == 1) {
            if (visit[next] == 0) {
                dfs(next);
            }
            else if(visit[next] == 1){
                flag = 0;
            }
        }
    }
    
    visit[now] = 2;
    
    print[a++] = now;
}
int main(){
    
    int a, b;
    
    scanf("%d", &n);
    
    while(scanf("%d %d", &a, &b) != EOF){
        graph[a][b] = 1;
    }
    
    for(int i = 1; i<=n; i++){
        if(visit[i] == 0)   dfs(i);
    }
    
    for(int i = 1; i<=n; i++){
        if(visit[i] != 2){
            flag = 0;
            break;
        }
    }
    
    if(flag == 1){
        printf("1\n");
        for(int i = n; i>=1; i--){
            printf("%d ", print[i]);
        }
        printf("\n");
    }
    else{
        printf("0\n");
    }
    
    return 0;
}
