
#include <stdio.h>
#include <stdlib.h>

// Define the structure of a Node
struct Node {
    int data;
    struct Node* next;
};

// Function to traverse the linked list using recursion
void traverse_linkedlist_recursion(struct Node** head) {

    // Create a pointer to the current node
    struct Node* ptr = *head;

    // Base case
    if (ptr == NULL) {
        printf("NULL");
        return;
    }

    // Print the data of the current node
    printf("%d -> ", ptr->data);

    // Recursively move to the next node
    traverse_linkedlist_recursion(&(ptr->next));
}

int main() {

    // Create pointers for three nodes
    struct Node* head = NULL;
    struct Node* sec = NULL;
    struct Node* third = NULL;

    // Dynamically allocate memory for the nodes
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

    // Traverse the linked list using recursion
    traverse_linkedlist_recursion(&head);

    return 0;
}

