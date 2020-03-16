//2015005078_정진교_A
#include<stdio.h>
#include<queue>
#include<vector>
#include<iostream>

using namespace std;

char a[501];
char b[501];
int arr[501][501];
int back[501][501];

void printA(int i, int j){
    
    if(i == 0 || j == 0)    return;
    
    if(back[i][j] == 4){
        printA(i-1, j-1);
        printf("%c", a[i]);
    }
    else if(back[i][j] == 3){
        printA(i-1, j);
    }
    else if(back[i][j] == 2){
        printA(i, j-1);
    }
}
void printB(int i, int j){
    
    if(i == 0 || j == 0)    return;
    
    if(back[i][j] == 4){
        printB(i-1, j-1);
        printf("%c", b[i]);
    }
    else if(back[i][j] == 3){
        printB(i-1, j);
    }
    else if(back[i][j] == 2){
        printB(i, j-1);
    }
}
int main(){
    
    scanf("%s", a+1);
    scanf("%s", b+1);
    
    int n = 0;
    int m = 0;
    
    for(int i = 1; i<501; i++){
        if(a[i] == '\0')    break;
        n++;
    }
    for(int i = 1; i<501; i++){
        if(b[i] == '\0')    break;
        m++;
    }

    if(n>=m){
        for(int i = 1; i<=m; i++){
            for(int j = 1; j<=n; j++){
                if(a[j] == b[i]){
                    arr[i][j] = arr[i-1][j-1] + 1;
                    back[i][j] = 4;
                }
                else{
                    if(arr[i-1][j]>= arr[i][j-1]){
                        arr[i][j] = arr[i-1][j];
                        back[i][j] = 3;
                    }
                    else{
                        arr[i][j] = arr[i][j-1];
                        back[i][j] = 2;
                    }
                }
            }
        }
        printB(m, n);
    }
    else{
        for(int i = 1; i<=n; i++){
            for(int j = 1; j<=m; j++){
                if(a[i] == b[j]){
                    arr[i][j] = arr[i-1][j-1] + 1;
                    back[i][j] = 4;
                }
                else{
                    if(arr[i-1][j]>= arr[i][j-1]){
                        arr[i][j] = arr[i-1][j];
                        back[i][j] = 3;
                    }
                    else{
                        arr[i][j] = arr[i][j-1];
                        back[i][j] = 2;
                    }
                }
            }
        }
        printA(n, m);
    }
    printf("\n");

    return 0;
}

