//2015005078_정진교_A
#include <stdio.h>
#define INF 987654321

int p[101];
int m[101][101];
int s[101][101];
void func(int i, int j){
    if(i == j)  printf("%d", i);
    else{
        printf("(");
        func(i, s[i][j]);
        func(s[i][j]+1, j);
        printf(")");
    }
}
int main(){
    
    int n;
    
    scanf("%d", &n);
    
    for(int i = 0; i<=n; i++)   scanf("%d", p+i);

    for(int l = 2; l<=n; l++){
        for(int i = 1; i<=n-l+1; i++){
            int j = i + l - 1;
            m[i][j] = INF;
            for(int k = i; k<=j-1; k++){
                int temp = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
                if(temp < m[i][j]){
                    m[i][j] = temp;
                    s[i][j] = k;
                }
            }
        }
    }
    printf("%d\n", m[1][n]);
    
    func(1, n);
    printf("\n");
    
    return 0;
}

