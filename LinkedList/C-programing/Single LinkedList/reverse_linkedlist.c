#include <stdio.h>
#include <stdlib.h>

/*
    Node structure for the Linked List
*/
struct Node{
    int data;
    struct Node* next;
};


/*
    Function: traverse_linkedlist

    Purpose:
    Traverses the linked list and prints
    each node's data.
*/
void traverse_linkedlist(struct Node** head){

    struct Node* ptr = *head;

    while(ptr != NULL){
        printf("%d -> ", ptr->data);
        ptr = ptr->next;
    }

    printf("NULL");
}


/*
    Function: reverse_linkedlist

    Purpose:
    Reverses the linked list using three pointers:
        1. curr
        2. next
        3. prev
*/
void reverse_linkedlist(struct Node** head){

    struct Node* curr = *head;
    struct Node* next = NULL;
    struct Node* prev = NULL;

    /*
        Reverse the direction of each node
    */
    while(curr != NULL){

        // Store the next node
        next = curr->next;

        // Reverse the current node's pointer
        curr->next = prev;

        // Move prev to current node
        prev = curr;

        // Move curr to the next node
        curr = next;
    }

    printf("\n\nAfter Reversing the Linked List:\n");
    printf("--------------------------------\n");

    traverse_linkedlist(&prev);
}


/*
    Main Function
*/
int main(){

    /*
        Creating pointers for each node
    */
    struct Node* head = NULL;
    struct Node* sec = NULL;
    struct Node* third = NULL;
    struct Node* four = NULL;
    struct Node* fifth = NULL;


    /*
        Dynamically allocating memory
        for each node
    */
    head = (struct Node*)malloc(sizeof(struct Node));
    sec = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    four = (struct Node*)malloc(sizeof(struct Node));
    fifth = (struct Node*)malloc(sizeof(struct Node));


    /*
        Creating the Linked List

        10 -> 20 -> 30 -> 40 -> 50 -> NULL
    */

    head->data = 10;
    head->next = sec;

    sec->data = 20;
    sec->next = third;

    third->data = 30;
    third->next = four;

    four->data = 40;
    four->next = fifth;

    fifth->data = 50;
    fifth->next = NULL;


    /*
        Display Original Linked List
    */
    printf("Original Linked List:\n");
    printf("---------------------\n");

    traverse_linkedlist(&head);


    /*
        Reverse the Linked List
    */
    reverse_linkedlist(&head);


    /*
        Complexity Analysis

        Time Complexity:
        O(n)

        The linked list is traversed once while
        reversing the links.

        Space Complexity:
        O(1)

        Only a constant number of pointers are used.
    */

    printf("\n\nComplexity Analysis:\n");
    printf("-------------------\n");
    printf("Time Complexity  : O(n)\n");
    printf("Space Complexity : O(1)\n");


    return 0;
}
