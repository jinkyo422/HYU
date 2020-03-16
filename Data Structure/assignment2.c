#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int arraySize = 100;
typedef struct stack * Stack;

struct stack {
    char * array;
    int size;
    int top;
};

Stack createStack(int arraySize){
    
    Stack S = (Stack)malloc(sizeof(struct stack));
    
    S->size = arraySize;
    S->top = -1;
    S->array = (char*)malloc(sizeof(char)*arraySize);
    
    return S;
    
}
Stack makeEmptyStack(Stack S){  //데이터 지우기
    
    free(S->array);
    S->array = (char*)malloc(sizeof(char)*arraySize);
    
    return S;
}
int isFull(Stack S){
    
    return (S->top == S->size);
}
int isEmpty(Stack S){
    
    return (S->top == -1);
}
void push(char X, Stack S){
    
    if(isFull(S)){
        printf("공간 부족\n");
        return;
    }
    
    S->array[++S->top] = X;
}
char pop(Stack S){
    
    if(isEmpty(S)){
        printf("스택에 아무 것도 없음\n");
        return '\0';
    }
    
    return S->array[S->top--];
}
void deleteStack(Stack S){  //free
    free(S);
}
int main(){
    
    int i, j, flag, exit = 1;
    char X, a[arraySize];
    char K;
    Stack S = NULL;
    
    S = createStack(arraySize);
    
    while(1){
        j = 0;
        flag = 0;
        for(i = 0; i<2*arraySize; i++){
            scanf("%c", &X);
            if(X == '!') {
                exit = 0;
                break;
            }
            if(X == '#')    break;
            if(X == ' ')    continue;
            
            if(X == '('){
                flag++;
            }
            if(flag){
                push(X, S);
                
                if(X == ')'){
                    flag--;
                    
                    while(1){
                        if(S->array[S->top] == '(') {
                            K = pop(S);
                            break;
                        }
                        K = pop(S);
                        if(K >= 'a' && K <= 'z')
                            a[j++] = K;
                    }
                }
            }
            else if (X == ')')
                flag--;
            else if (flag < 0)
                continue;
            else
                a[j++] = X;
        }
        makeEmptyStack(S);
        if(exit == 0)   break;
        
        if(flag == 0)  printf("right. ");
        else    printf("wrong. ");
        
        for(i = 0; i<j; i++){
            printf("%c ", a[i]);
        }
        
        printf("\n");
        scanf("%c", &X);
    }
    deleteStack(S);
}

