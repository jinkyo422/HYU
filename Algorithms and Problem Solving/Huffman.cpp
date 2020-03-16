//2015005078_정진교_A
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

using namespace std;

struct nodetype;
typedef nodetype * tree;

typedef struct nodetype{
    char str;
    int num;
    tree left;
    tree right;
    int level;
}node;
char temp1[4];
tree heap[400000];
int now, sum;
tree merge(tree left, tree right){
    tree temp = (tree)malloc(sizeof(node));
    temp->num = left->num + right->num;
    temp->str = '?';
    temp->left = left;
    temp->right = right;
    return temp;
}
void heap_tree(){
    int pos = now;
    int temp = now;
    for (int i = temp / 2; i > 0; i /= 2){
        if (heap[i]->num > heap[pos]->num)
            swap(heap[i], heap[pos]);
        pos /= 2;
    }
}
tree delete_min(){
    tree MIN = heap[1];
    swap(heap[1], heap[now]);
    now--;
    
    int i = 1, child = 2;
    while (child <= now){
        
        if (child<now && heap[child]->num > heap[child + 1]->num) {
            child++;
        }
        if (heap[i]->num <= heap[child]->num) break;
        swap(heap[i], heap[child]);
        i = child;
        child *= 2;
    }
    return MIN;
}
void search_ans(tree now, int level){
    now->level = level;
    if(now->str != '?')sum += now->num * now->level;
    if (now->left != NULL)
        search_ans((now->left), level + 1);
    if (now->right != NULL)
        search_ans((now->right), level + 1);
    return;
}
int main(){
    
    int n, count = 1;
    scanf("%d", &n);
    
    for (int i = 1; i <= n; i++){
        int temp2;
        scanf("%s%d", temp1, &temp2);
        tree temp = (tree)malloc(sizeof(node));
        temp->num = temp2;
        temp->str = temp1[0];
        temp->level = 0;
        temp->left = NULL;
        temp->right = NULL;
        heap[i] = temp;
        now++;
        heap_tree();
    }
    int total;
    scanf("%d",&total);
    
    tree a, b;
    tree newnode = NULL;
    while (now > 0){
        a = delete_min();
        b = delete_min();
        newnode = merge(a, b);
        
        if (now == 0) break;
        now++;
        heap[now] = newnode;
        heap_tree();
    }
    search_ans(newnode, 0);
    
    int num = n-1;
    while(num/2 != 0){
        count++;
        num = num/2;
    }
    
    printf("%d\n", count*total);
    printf("%d\n", sum);
    
    return 0;
}

