#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define MAX_ELEMENTS 100000
#define HEAP_FULL(n) (n == MAX_ELEMENTS - 1)
#define HEAP_EMPTY(n) (!n)

typedef struct {
    int key;
} element;

element heap[MAX_ELEMENTS];

void insert_min_heap(element item, int* n) {
    
    int i = ++(*n);
    
    while(i != 1){
        
        if(abs(item.key) < abs(heap[i/2].key)){
            
            heap[i] = heap[i/2];
            i /= 2;
        }
        else if(abs(item.key) == abs(heap[i/2].key)){
            
            if(item.key < heap[i/2].key){
                
                heap[i] = heap[i/2];
                i /= 2;
            }
            else break;
        }
        else break;
    }
    heap[i] = item;
}
element delete_min_heap(int* n){
    
    element item, temp;
    int parent = 1, child = 2;
    
    if (HEAP_EMPTY(*n)) {
        
        item.key = 0;
        return item;
    }
    
    item = heap[1];
    temp = heap[(*n)--];
   
    while (child <= (*n)) {
        
        if ((child < (*n)) && (abs(heap[child].key) >= abs(heap[child+1].key))){
            
            if(abs(heap[child].key) == abs(heap[child+1].key)){
                
                if(heap[child].key > heap[child+1].key)
                    child++;
            }
            
            else    child++;
            
        }
        
        if (abs(temp.key) <= abs(heap[child].key))
            break;
        
        heap[parent] = heap[child];
        parent = child;
        child *= 2;
    }
    heap[parent] = temp;
    
    return item;
}

int main(){
    
    int q, i, n = 0;
    element e;
    
    scanf("%d", &q);
    
    while(q){
        
        scanf("%d", &i);
        
        switch (i) {
            case 0:
                e = delete_min_heap(&n);
                printf("%d\n", e.key);
                break;
                
            default:
                e.key = i;
                insert_min_heap(e, &n);
                break;
        }
        --q;
    }
}

