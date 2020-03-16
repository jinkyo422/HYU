#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct employee{
    
    char name[10];
    int age;
    int salary;
    char department[20];
    
}Employee;
int number;
Employee Empty = {0, 0, 0, 0};
void insert(Employee *people, char *word){
    int i;
    
    for(i = 0; i< number ; i++){
        if(strcmp(people[i].name, "") == 0) break;
    }
    
    if(i == number){
        printf("Not enough space\n");
        return;
    }
    
    word = strtok(NULL, " ");
    strcpy(people[i].name, word);
    
    word = strtok(NULL, " ");
    people[i].age = atoi(word);
    
    word = strtok(NULL, " ");
    people[i].salary = atoi(word);
    
    word = strtok(NULL, " ");
    strcpy(people[i].department, word);
}
void delete_one(Employee *people, char *word){
    int i;
    word = strtok(NULL, " ");
    
    for(i = 0; i<number; i++){
        if(strcmp(people[i].name, word) == 0)   break;
    }
    if(i == number){
        printf("Not found\n");
        return;
    }
    people[i] = Empty;
}
int find(Employee *people, char *word){
    int i;
    word = strtok(NULL, " ");
    
    for(i = 0; i<number; i++){
        if(strcmp(people[i].name, word) == 0)   break;
    }
    
    if(i == number) return -1;

    return i;
}
void inform(Employee *people, char *word){
    int i, count = 0;
    int j[number];
    word = strtok(NULL, " ");
    
    for(i = 0; i<=number; i++){
        if(strcmp(people[i].name, word) == 0){
            j[count] = i;
            count++;
        }
    }
    if(count == 0){
        printf("Not found\n");
        return;
    }
    for(i = 0; i<count; i++){
        printf("%s %d %d %s\n", people[j[i]].name, people[j[i]].age, people[j[i]].salary, people[j[i]].department);
    }
}
int avgBenefit(Employee *people, char *word){
   
    int i, sum= 0, count = 0;
    int j[number];
    
    word = strtok(NULL, " ");
    
    for(i = 0; i<number; i++){
        if(strcmp(people[i].department, word) == 0){
            j[count] = i;
            count++;
        }
    }
    if(count == 0)  return 0;
    
    for(i = 0; i<count; i++){
        sum = sum + people[j[i]].salary;
    }
    return sum/count;
}
int main(){
    char input[100];
    char *word;
    Employee *people = NULL;
    int flag = 0, i;
    
    gets(input);
    word = strtok(input, " ");
    
    if(word == NULL)    return 0;
    
    if(strcmp(word, "set") == 0){
        word = strtok(NULL, " ");
        number = atoi(word);
        people = (Employee*)malloc(sizeof(Employee)*number);
        flag = 1;
    }
    if(!flag)   return 0;
    
    for(i = 0; i<number; i++){
        people[i] = Empty;
    }
    
    while(1){
        
        gets(input);
        word = strtok(input, " ");
        
        if(word == NULL)    break;
        
        if(strcmp(word, "insert") == 0) insert(people, word);
        else if(strcmp(word, "delete") == 0) delete_one(people, word);
        else if(strcmp(word, "find") == 0) printf("%d\n", find(people, word));
        else if(strcmp(word, "inform") == 0) inform(people, word);
        else if(strcmp(word, "avg") == 0) printf("%d\n", avgBenefit(people, word));
    }
    
    free(people);
    return 0;
}
