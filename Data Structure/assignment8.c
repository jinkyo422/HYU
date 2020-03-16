#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_ELEMENTS 100000
#define HEAP_FULL(n) (n == MAX_ELEMENTS - 1)
#define HEAP_EMPTY(n) (!n)

typedef struct{
    char name[100];
    int ko;
    int en;
    int ma;
}student;
student heap[MAX_ELEMENTS];
int n;

int studentComp(student stu1, student stu2){
    if(stu1.ko != stu2.ko){
        if(stu1.ko > stu2.ko)   return -1;
        else    return 1;
    }
    else{
        if(stu1.en != stu2.en){
            if(stu1.en < stu2.en)   return -1;
            else    return 1;
        }
        else{
            if(stu1.ma != stu2.ma){
                if(stu1.ma > stu2.ma)   return -1;
                else    return 1;
            }
        }
    }
    return strcmp(stu1.name, stu2.name);
}
void adjust(int root, int n){
    int child;
    student rootStu;
    rootStu = heap[root];
    child = 2*root;
    while(child<=n){
        if((child<n) && (studentComp(heap[child], heap[child + 1]) > 0)){
            child += 1;
        }
        if(studentComp(rootStu, heap[child])<0){
            break;
        }
        else{
            heap[child/2] = heap[child];
            child *= 2;
        }
    }
    heap[child/2] = rootStu;
}
void mHeapsort(int n){
    int i;
    student temp;
    for(i = n/2; i > 0; i--) adjust(i, n);
    for(i = n-1; i > 0; i--){
        temp = heap[1];
        heap[1] = heap[i+1];
        heap[i+1] = temp;
        adjust(1, i);
    }
}

int main(){
    int num = 0;
    int i = 0;
    int tempKo, tempEn, tempMa;
    char tempName[100];
    scanf("%d", &num);
    for(i = 0; i< num; i++){
        scanf("%s %d %d %d", tempName, &tempKo, &tempEn, &tempMa);
        n = i + 1;
        heap[n].ko = tempKo;
        heap[n].en = tempEn;
        heap[n].ma = tempMa;
        strcpy(heap[n].name, tempName);
    }
    mHeapsort(n);
    
    for(i = n; i> 0; i—){
        printf("%s\n", heap[i].name);
    }
}
