#include <stdio.h>
#include <stdlib.h>

// Define the structure of a Node
struct Node {
    int data;
    struct Node* next;
};

// Function to traverse and display the linked list
void Traverse_linkedList(struct Node** head) {

    // Create a pointer to traverse the linked list
    struct Node* ptr = *head;

    // Traverse the list until NULL is reached
    while (ptr != NULL) {

        // Print the data of the current node
        printf("%d -> ", ptr->data);

        // Move to the next node
        ptr = ptr->next;
    }

    // Indicate the end of the linked list
    printf("NULL");

    return;
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

    // Traverse and display the linked list
    Traverse_linkedList(&head);

    return 0;
}

