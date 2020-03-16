#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node* Node;
typedef struct node* Tree;
typedef struct node{
    int value;
    Node parent;
    Node leftChild;
    Node rightChild;
}node;

Tree createTree(){
    Tree tmp = (Tree)malloc(sizeof(struct node));
    tmp->value = 0;
    tmp->leftChild = NULL;
    tmp->rightChild = NULL;
    tmp->parent = NULL;
    return tmp;
}
int isEmpty(Tree t){
    if(t->rightChild == NULL){
        return 1;
    }
    return 0;
}
Node search(Tree t, int key){
    if(t == NULL) return t;
    
    if(key>t->value) return search(t->rightChild, key);
    else if(key<t->value) return search(t->leftChild, key);
    
    return t;
}
void deleteNode(Tree t, int key){
    Node del = search(t, key);
    int dif = 0;
    if(del == NULL){
        printf("Not Found\n");
        return;
    }
    if(del->parent->leftChild == del){
        dif = 0;
    }
    else {
        dif = 1;
    }
    Node tmp;
    int value = 0;
    if(del->leftChild == NULL && del->rightChild == NULL){
        if(dif == 0)    del->parent->leftChild = NULL;
        else    del->parent->rightChild = NULL;
        free(del);
    }
    else if(del->leftChild != NULL && del->rightChild == NULL){
        if(dif == 0)    del->parent->leftChild = del->leftChild;
        else    del->parent->rightChild = del->leftChild;
        free(del);
    }
    else if(del->leftChild == NULL && del->rightChild != NULL){
        if(dif == 0)    del->parent->leftChild = del->rightChild;
        else    del->parent->rightChild = del->rightChild;
        free(del);
    }
    else{
        tmp = del->leftChild;
        value = tmp->value;
        while(tmp->rightChild != NULL){
            tmp = tmp->rightChild;
            value = tmp->value;
        }
        deleteNode(t, value);
        del->value = value;
    }
}
void insertNode(Tree t, int key){
    Node parent1 = NULL, parent2 = NULL;
    Node tmp;
    if(isEmpty(t)){
        tmp = createTree();
        tmp->value = key;
        tmp->parent = t;
        t->rightChild = tmp;
        return;
    }
    else{
        parent1 = t->rightChild;
        t = createTree();
        t->value = key;
        if (key < parent1->value) {
            while (parent1 != NULL) {
                if (key < parent1->value) {
                    parent2 = parent1;
                    parent1 = parent1->leftChild;
                }
                else {
                    parent2 = parent1;
                    parent1 = parent1->rightChild;
                }
            }
            if (key < parent2->value){
                parent2->leftChild = t;
                t->parent = parent2;
            }
            else{
                parent2->rightChild = t;
                t->parent = parent2;
            }
        }
        else {
            while (parent1 != NULL) {
                if (key < parent1->value) {
                    parent2 = parent1;
                    parent1 = parent1->leftChild;
                }
                else {
                    parent2 = parent1;
                    parent1 = parent1->rightChild;
                }
            }
            if (key < parent2->value){
                parent2->leftChild = t;
                t->parent = parent2;
            }
            else{
                parent2->rightChild = t;
                t->parent = parent2;
            }
            return;
        }
    }
}
void showAll(Tree t){
    if(t){
        showAll(t->leftChild);
        printf("%d ", t->value);
        showAll(t->rightChild);
    }
}
int getHeight(Tree t, int key){
    
    int height = 0;
    
    if(t != NULL){
        
        if(getHeight(t->leftChild, key) > getHeight(t->rightChild, key))
            height = 1 + getHeight(t->leftChild, key);
        
        else
            height = 1 + getHeight(t->rightChild, key);
    }
    
    return height;
}
int main(){
    
    char input[3];
    char *word;
    int a;
    
    Tree root = createTree();
    
    while(1){
        
        gets(input);
        word = strtok(input, " ");
        
        if(word == NULL)    break;
        
        if(strcmp(word, "i") == 0){
            word = strtok(NULL, " ");
            a = atoi(word);
            
            insertNode(root, a);
        }
        
        else if(strcmp(word, "d") == 0){
            word = strtok(NULL, " ");
            a = atoi(word);
            
            deleteNode(root, a);
        }
        
        else if(strcmp(word, "h") == 0) {
            word = strtok(NULL, " ");
            a = atoi(word);
            
            if(search(root, a) == NULL) printf("Not found\n");
            
            else    printf("The height of the node (%d) is %d\n", a, getHeight(search(root, a), a)-1);
        }
        
        else if(strcmp(word, "s") == 0){
            showAll(root->rightChild);
            printf("\n");
        }
        
        else if(strcmp(word, "e") == 0) break;
    }
}

