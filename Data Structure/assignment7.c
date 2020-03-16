#include <stdio.h>

#define INF 1000000000

int node[1001][1001];
int dist[1001];
int visit[1001];
int n, m;

int dijkstra(int start, int end){
    
    int min = INF;
    int min_v = 0;
    int t, i, j;
    
    dist[start] = 0;
    
    for(t = start; t<= n; t++){
        min = INF;
        min_v = start;
        
        for(i = start; i<=n; i++){
            if(visit[i] == 0 && min > dist[i]){
                min = dist[i];
                min_v = i;
            }
        }
        visit[min_v] = 1;
        
        for(j = start; j<= n; j++){
            if(dist[j] > dist[min_v] + node[min_v][j]){
                dist[j] = dist[min_v] + node[min_v][j];
            }
        }
    }
    
    return dist[end];
}

int main(){
    
    int i, j, u, v, w;
    int start, end;
    
    scanf("%d", &n);
    scanf("%d", &m);
    
    for(i = 1; i<=n; i++){
        for(j = 1; j<=n; j++){
            node[i][j] = INF;
        }
    }
    
    for(i = 0; i<m; i++){
        scanf("%d %d %d", &u, &v, &w);
        node[u][v] = w;
    }
    
    for(i = 1; i<=n; i++)   dist[i] = INF;
    
    scanf("%d %d", &start, &end);
    
    printf("%d\n", dijkstra(start, end));
}

