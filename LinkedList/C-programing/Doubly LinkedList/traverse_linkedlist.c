/*
    Doubly Linked List Traversal

    This program demonstrates:

    1. Forward traversal using the next pointer
    2. Backward traversal using the prev pointer

    Example:

    Forward:
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL

    Backward:
    6 -> 5 -> 4 -> 3 -> 2 -> 1 -> NULL
*/

#include <stdio.h>
#include <stdlib.h>


/*
    Node structure for the Doubly Linked List

    Each node contains:
        data -> stores the value
        next -> points to the next node
        prev -> points to the previous node
*/
struct Node{

    int data;

    struct Node* next;
    struct Node* prev;
};


/*
    Function: traverse_forward

    Purpose:
    Traverses the linked list from head to tail.

    Direction:
    Uses the next pointer.
*/
void traverse_forward(struct Node** head){

    struct Node* ptr = *head;

    while(ptr != NULL){

        printf("%d -> ", ptr->data);

        ptr = ptr->next;
    }

    printf("NULL");
}


/*
    Function: traverse_backward

    Purpose:
    Traverses the linked list from tail to head.

    Direction:
    Uses the prev pointer.
*/
void traverse_backward(struct Node** tail){

    struct Node* ptr = *tail;

    while(ptr != NULL){

        printf("%d -> ", ptr->data);

        ptr = ptr->prev;
    }

    printf("NULL");
}


int main(){

    /*
        Creating pointers for each node
    */
    struct Node* head = NULL;
    struct Node* sec = NULL;
    struct Node* third = NULL;
    struct Node* fourth = NULL;
    struct Node* fifth = NULL;
    struct Node* tail = NULL;


    /*
        Dynamically allocating memory
        for each node
    */
    head = (struct Node*)malloc(sizeof(struct Node));
    sec = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    fourth = (struct Node*)malloc(sizeof(struct Node));
    fifth = (struct Node*)malloc(sizeof(struct Node));
    tail = (struct Node*)malloc(sizeof(struct Node));


    /*
        Creating the Doubly Linked List

        1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
    */


    /*
        First Node
    */
    head->prev = NULL;
    head->data = 1;
    head->next = sec;


    /*
        Second Node
    */
    sec->prev = head;
    sec->data = 2;
    sec->next = third;


    /*
        Third Node
    */
    third->prev = sec;
    third->data = 3;
    third->next = fourth;


    /*
        Fourth Node
    */
    fourth->prev = third;
    fourth->data = 4;
    fourth->next = fifth;


    /*
        Fifth Node
    */
    fifth->prev = fourth;
    fifth->data = 5;
    fifth->next = tail;


    /*
        Last Node / Tail
    */
    tail->data = 6;
    tail->prev = fifth;
    tail->next = NULL;


    /*
        Forward Traversal

        Start from head and follow
        the next pointer.
    */
    printf("Moving Forward ------->\n");
    printf("--------------------------------------------\n");

    traverse_forward(&head);


    /*
        Backward Traversal

        Start from tail and follow
        the prev pointer.
    */
    printf("\n\nMoving from Backward ------->\n");
    printf("--------------------------------------------\n");

    traverse_backward(&tail);


    /*
        Complexity Analysis

        Forward Traversal:
        Time Complexity : O(n)
        Space Complexity: O(1)

        Backward Traversal:
        Time Complexity : O(n)
        Space Complexity: O(1)

        Only one pointer is used for traversal,
        so no additional data structure is required.
    */
    printf("\n\nComplexity Analysis:\n");
    printf("-------------------\n");
    printf("Forward Traversal  : O(n) Time, O(1) Space\n");
    printf("Backward Traversal : O(n) Time, O(1) Space\n");


    return 0;
}

