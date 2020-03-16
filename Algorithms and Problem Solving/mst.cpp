//2015005078_정진교_A
#include<stdio.h>
#include<iostream>
#include<queue>
#include<vector>

using namespace std;

struct Edge{
    int from;
    int to;
    int weight;
    Edge(int a, int b, int c) : from(a), to(b), weight(c) {}
};
bool operator < (Edge small, Edge big){
    
    if(small.weight == big.weight){
        if(small.from == big.from){
            return small.to > big.to;
        }
        return small.from > big.from;
    }
    return small.weight > big.weight;
}

int n;
int arr[1001];
vector<Edge> edge;
priority_queue<Edge> Q;
priority_queue<Edge> Q2;

int find(int a){
    
    if (arr[a] != a) {
        return arr[a] = find(arr[a]);
    }
    return arr[a];
}
void uni(int a, int b){
    arr[find(b)] = find(a);
}
int main(){
    
    int a, b, c, count = 0;
    
    
    scanf("%d", &n);
    
    for(int i = 1; i<=n; i++)   arr[i] = i;
    
    while(scanf("%d %d %d", &a, &b, &c) != EOF){
        if(a < b){
            Edge e = Edge(a, b, c);
            edge.push_back(e);
        }
        else{
            Edge e = Edge(b, a, c);
            edge.push_back(e);
        }
    }
    
    int size = (int)edge.size();
    
    for(int i = 0; i<size; i++){
        Q.push(edge[i]);
    }
    
    while(!Q.empty()){
        Edge e = Q.top();
        Q.pop();
        
        int u = find(e.from);
        int v = find(e.to);
        
        if(u != v){
            uni(u, v);
            Q2.push(e);
            count++;
        }
    }
    
    printf("%d\n", count);
    
    while(!Q2.empty()){
        Edge e = Q2.top();
        Q2.pop();
        
        printf("%d %d %d\n", e.from, e.to, e.weight);
    }
    
    return 0;
}
