//2015005078_정진교_A
#include<stdio.h>
#include<queue>
#include<vector>
#include<iostream>

using namespace std;

#define INF 987654321

typedef pair<int, int> pii;
vector<pii> list[5001];
pii a;
priority_queue<pii, vector<pii>, greater<pii> > Q;

int d[5001];
int V, E;

void dijkstra(int k){
    d[k] = 0;
    a.first = 0;
    a.second = k;
    Q.push(a);
    while(!Q.empty()){
        pii u = Q.top();
        Q.pop();
        int weight = u.first;
        int vertex = u.second;
        if (d[vertex] < weight) continue;
        for(int i = 0; i < list[vertex].size(); i++){
            int nextV = list[vertex][i].first;
            int nextW = list[vertex][i].second;
            if(d[nextV] > d[vertex] + nextW){
                d[nextV] = d[vertex] + nextW;
                a.first = d[nextV];
                a.second = nextV;
                Q.push(a);
            }
        }
    }
}
int main(){
    
    int n;
    
    scanf("%d", &n);
    
    for(int i = 1; i<=n; i++)   d[i] = INF;
    
    for(int i = 1; i<=n; i++){
        int u, v, w, temp;
        scanf("%d %d", &u, &temp);
        for(int j = 1; j<=temp; j++){
            scanf("%d %d", &v, &w);
            a.first = v;
            a.second = w;
            list[u].push_back(a);
        }
    }
    
    dijkstra(1);
    
    int temp = 0;
    
    for(int i = 1; i<=n; i++){
        if(temp < d[i])  temp = d[i];
    }
    
    printf("%d\n", temp);
    
    return 0;
}
