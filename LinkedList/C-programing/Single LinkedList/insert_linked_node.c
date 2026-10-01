
#include <stdio.h>
#include <stdlib.h>

// Node structure for the linked list
struct Node{
    int data;
    struct Node* next;
};

// Traverse and display the linked list
void Traverse_linkedList(struct Node** head){

    struct Node* ptr = *head;

    while(ptr != NULL){
        printf("%d -> ",ptr->data);
        ptr = ptr->next;
    }

    printf("NULL");
    return;
}

// Insert a new node at the beginning of the linked list
void Insert_Node_inBegning(struct Node** head){

    struct Node* newNode = NULL;

    // Allocate memory for the new node
    newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->data = 5;

    // Connect the new node with the current head
    newNode->next = *head;

    // Display the linked list after insertion
    Traverse_linkedList(&newNode);
}

// Insert a new node before the node containing the given key
void Insert_node_inSpecificPlace(struct Node** head, int key){

    struct Node* NewNode = NULL;
    struct Node* prev = NULL;

    // Allocate memory for the new node
    NewNode = (struct Node*)malloc(sizeof(struct Node));

    struct Node* ptr = *head;

    // Search for the node containing the given key
    while(ptr != NULL && ptr->data != key){
        prev = ptr;
        ptr = ptr->next;
    }

    NewNode->data = 15;

    // Connect the new node between prev and ptr
    NewNode->next = prev->next;
    prev->next = NewNode;

    // Display the linked list after insertion
    Traverse_linkedList(head);
}

// Insert a new node after the node containing the given key
void Insert_Node_inEnd(struct Node** head, int key){

    struct Node* newEnd = NULL;
    struct Node* temp = NULL;

    // Allocate memory for the new node
    newEnd = (struct Node*)malloc(sizeof(struct Node));

    struct Node* ptr = *head;

    // Search for the node containing the given key
    while(ptr != NULL){

        if(ptr->data == key){
            temp = ptr;
            break;
        }

        ptr = ptr->next;
    }

    // Connect the new node after the found node
    temp->next = newEnd;

    newEnd->data = 40;
    newEnd->next = NULL;

    // Display the linked list after insertion
    Traverse_linkedList(head);
}

int main(){

    struct Node* head = NULL;
    struct Node* sec = NULL;
    struct Node* third = NULL;

    // Allocate memory for three nodes
    head = (struct Node*)malloc(sizeof(struct Node));
    sec = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));

    // Initialize the first node
    head->data = 10;
    head->next = sec;

    // Initialize the second node
    sec->data = 20;
    sec->next = third;

    // Initialize the third node
    third->data = 30;
    third->next = NULL;

    // Display the original linked list
    printf("ORIGINAL LINKED LIST ------------->\n");
    Traverse_linkedList(&head);

    // Insert a new node at the beginning
    printf("\nADDING NEW NODE AT BEGINNING ------------->\n");
    Insert_Node_inBegning(&head);

    // Insert a new node at a specific position
    printf("\nAdding New Node At the Specific Place ------------>\n");
    Insert_node_inSpecificPlace(&head, 20);

    // Insert a new node at the end
    printf("\nADDING NEW NODE AT END --------->\n");
    Insert_Node_inEnd(&head, 30);

    return 0;
}

