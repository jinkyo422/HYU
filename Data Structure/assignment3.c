#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node * pNode;
typedef pNode List;
typedef pNode Node;

struct node{
    int value;
    Node next;
};

List makeEmptyList(List L){
    L->value = 0;
    L->next = NULL;
    
    return L;
}
void insert(int v, List L, Node N){
    List new = (List)malloc(sizeof(struct node));
    
    new->value = v;
    new->next = N->next;
    N->next = new;
}
void delete(int v, List L){
    Node move1 = L->next;
    Node move2 = L;
    
    while (move1 != NULL){
        if(move1->value == v){
            move2->next = move1->next;
            free(move1);
            break;
        }
        move1 = move1->next;
        move2 = move2->next;
    }
}
Node findPrev(int v, List L){
    Node move1 = L->next;
    Node move2 = L;

    
    while (move1 != NULL){
        if(move1->value == v){
            break;
        }
        move1 = move1->next;
        move2 = move2->next;
    }
    
    return move2;
}
Node find(int v, List L){
    Node move = L->next;
    
    while (move!=NULL){
        if(move->value == v)    break;
        move = move->next;
    }
    return move;
}
void deleteList(List L){
    Node move;
    
    while(L){
        move = L;
        L = L->next;
        free(move);
    }
}
void show(Node N){
    Node move = N->next;
    while(move!=NULL){
        printf("%d ", move->value);
        move = move->next;
    }
    printf("\n");
}

int main(){
    
    char input[5];
    char *word;
    int a, b;
    
    List head = (List)malloc(sizeof(struct node));
    
    Node temp1 = NULL;
    Node temp2 = NULL;
    
    makeEmptyList(head);
    
    while(1){
        
        gets(input);
        word = strtok(input, " ");
        
        if(word == NULL)    break;
        
        if(strcmp(word, "i") == 0){
            word = strtok(NULL, " ");
            a = atoi(word);
            
            word = strtok(NULL, " ");
            b = atoi(word);
            
            if(b==0){
                insert(a, head, head);
                continue;
            }
            
            temp1 = find(b, head);
            
            if(temp1 == NULL){
                printf("Insert error. The %d isn't in the list.\n", b);
                continue;
            }
            insert(a, head, temp1);
        }
        
        else if(strcmp(word, "d") == 0){
            word = strtok(NULL, " ");
            a = atoi(word);
            
            temp1 = find(a, head);
            
            if(temp1 == NULL){
                printf("Delete error. The %d isn't in the list.\n", a);
                continue;
            }
            
            delete(a, head);
        }
        
        else if(strcmp(word, "f") == 0) {
            word = strtok(NULL, " ");
            a = atoi(word);
            
            temp1 = find(a, head);
            
            if(temp1 == NULL){
                printf("Find error. The %d isn't in the list.\n", a);
                continue;
            }
            
            temp2 = findPrev(a, head);
            
            if(temp2->value == 0){
                printf("The %d is next of The header.\n", a);
                continue;
            }
            
            printf("The %d is next of The %d.\n", a, temp2->value);
        }
        
        else if(strcmp(word, "s") == 0) show(head);
        
        else if(strcmp(word, "e") == 0) break;
        
    }
    deleteList(head);
    
}

