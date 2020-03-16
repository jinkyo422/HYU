#include <stdio.h>

int matrix[1001][1001];
int visit[1001];
int visit2[1001];
int queue[1001];
int n, m, v;
int rear, front;

void dfs(int now) {
    printf("%d ", now);
    visit[now] = 1;
    
    for (int j = 1; j <= n; j++) {
        int next = j;
        if (matrix[now][next] == 1) {
            if (visit[next] == 0) {
                dfs(next);
            }
        }
    }
}
void bfs(int start){
    
    printf("%d ", start);
    queue[0] = start;
    rear++;
    visit2[start] = 1;
    
    while(front<rear){
        int now = queue[front++];
        
        for(int j = 1; j<= n; j++){
            int next = j;
            if(matrix[now][next] == 1){
                if(visit2[next] == 0){
                    visit2[next] = 1;
                    printf("%d ", j);
                    queue[rear++] = j;
                }
            }
        }
    }
    
}
int main(){
    
    int i, row, col;
    
    scanf("%d %d %d", &n, &m, &v);
    
    for(i = 0; i<m; i++){
        scanf("%d %d", &row, &col);
        matrix[row][col] = matrix[col][row] = 1;
    }
    
    dfs(v);
    printf("\n");
    bfs(v);
    printf("\n");
    
}

