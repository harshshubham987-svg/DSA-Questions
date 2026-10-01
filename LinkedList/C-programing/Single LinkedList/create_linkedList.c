
#include <stdio.h>
#include <stdlib.h>

// Define the structure of a Node
struct Node {
    int data;
    struct Node* next;
};

int main() {

    // Create three node pointers
    struct Node* head = NULL;
    struct Node* sec = NULL;
    struct Node* third = NULL;

    // Dynamically allocate memory for three nodes
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

    // Start traversal from the head node
    struct Node* ptr = head;

    // Traverse the linked list until NULL is reached
    while (ptr != NULL) {

        // Print the data of the current node
        printf("%d -> ", ptr->data);

        // Move to the next node
        ptr = ptr->next;
    }

    // Mark the end of the linked list
    printf("NULL");

    return 0;
}

