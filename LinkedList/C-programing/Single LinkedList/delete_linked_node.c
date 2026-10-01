
#include <stdio.h>
#include <stdlib.h>

// Define the structure of a Node
struct Node {
    int data;
    struct Node* next;
};

// Function to traverse and display the linked list
void Traverse_linkedList(struct Node** head) {

    // Pointer to traverse the linked list
    struct Node* ptr = *head;

    // Traverse until the end of the linked list
    while (ptr != NULL) {

        // Print the current node's data
        printf("%d -> ", ptr->data);

        // Move to the next node
        ptr = ptr->next;
    }

    // Mark the end of the linked list
    printf("NULL");

    return;
}

// Function to delete the head node
void Delete_head_Node(struct Node** head, int key) {

    // Store the current head node
    struct Node* temp = *head;

    // Check if the head node exists
    // and contains the given key
    if (temp != NULL && temp->data == key) {

        // Move the head pointer to the next node
        *head = temp->next;

        // Free the memory of the old head node
        free(temp);
    }

    printf("\nThe Linked List After Deleting First(head) Node ----------->\n");

    // Display the linked list after deletion
    Traverse_linkedList(head);

    return;
}

// Function to delete the last node
void Delete_End_node(struct Node** head) {

    // Pointers used to track the previous
    // and current nodes
    struct Node* prev = NULL;
    struct Node* temp = NULL;

    // Pointer used to traverse the linked list
    struct Node* ptr = *head;

    // Traverse to the last node
    while (ptr != NULL) {

        // Keep track of the previous node
        prev = temp;

        // Update the current node
        temp = ptr;

        // Move to the next node
        ptr = ptr->next;
    }

    // Remove the last node from the list
    prev->next = NULL;

    // Free the memory of the last node
    free(temp);

    printf("\nThe linked List After Deleting the Last Node------>\n");

    // Display the linked list after deletion
    Traverse_linkedList(head);
}

// Function to delete a specific node
void Delete_specific_node(struct Node** head, int key) {

    // Pointers used to track the nodes
    struct Node* temp = NULL;
    struct Node* prev = NULL;
    struct Node* ptr = *head;

    // Traverse until the required node is found
    while (ptr != NULL && ptr->data != key) {

        // Store the previous node
        prev = temp;

        // Move temp to the next node
        temp = ptr->next;

        // Move ptr to the next node
        ptr = ptr->next;
    }

    // Connect the previous node
    // to the node after the target node
    prev->next = temp->next;

    // Free the target node
    free(temp);

    printf("\n The Linked List After deleting the specific(%d) Node --------->\n", key);

    // Display the linked list after deletion
    Traverse_linkedList(head);

    return;
}

int main() {

    // Create pointers for six nodes
    struct Node* head = NULL;
    struct Node* sec = NULL;
    struct Node* third = NULL;
    struct Node* fourth = NULL;
    struct Node* fifth = NULL;
    struct Node* sixth = NULL;

    // Dynamically allocate memory for six nodes
    head = (struct Node*)malloc(sizeof(struct Node));
    sec = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    fourth = (struct Node*)malloc(sizeof(struct Node));
    fifth = (struct Node*)malloc(sizeof(struct Node));
    sixth = (struct Node*)malloc(sizeof(struct Node));

    // Initialize the first node
    head->data = 10;
    head->next = sec;

    // Initialize the second node
    sec->data = 20;
    sec->next = third;

    // Initialize the third node
    third->data = 30;
    third->next = fourth;

    // Initialize the fourth node
    fourth->data = 40;
    fourth->next = fifth;

    // Initialize the fifth node
    fifth->data = 50;
    fifth->next = sixth;

    // Initialize the sixth node
    sixth->data = 60;
    sixth->next = NULL;

    // Display the original linked list
    printf("The Original Linked List------>\n");
    Traverse_linkedList(&head);

    // Delete the first (head) node
    Delete_head_Node(&head, 10);

    // Delete the last node
    Delete_End_node(&head);

    // Delete a specific node
    Delete_specific_node(&head, 40);

    return 0;
}

