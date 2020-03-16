//2015005078_정진교_A
#include <stdio.h>
#include <algorithm>

using namespace std;
int a[100001];
int b[100001];
int main(){
    
    int n, m, count = 0, temp;
    
    scanf("%d %d", &n, &m);
    
    for(int i = 1; i<=n; i++){
        scanf("%d", &temp);
        a[temp] = 1;
    }
    for(int i = 1; i<=m; i++){
        scanf("%d", &temp);
        b[temp] = 1;
    }
    
    for(int i = 1; i<=100000; i++){
        if(a[i] == 1 && b[i] == 1){
            count++;
        }
    }
    
    printf("%d\n", count);
    
    return 0;
}
