/*
    Doubly Linked List

    This program demonstrates:

    1. Creating a Doubly Linked List
    2. Traversing the list from Forward direction
    3. Traversing the list from Backward direction

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

        head
         |
         v
        1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
                                      ^
                                      |
                                     tail
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
    struct Node* ptr = head;

    printf("Moving Forward ------->\n");
    printf("--------------------------------------------\n");

    while(ptr != NULL){

        printf("%d -> ", ptr->data);

        ptr = ptr->next;
    }

    printf("NULL");


    /*
        Backward Traversal

        Start from tail and follow
        the prev pointer.
    */
    printf("\n\nMoving from Backward ------->\n");
    printf("--------------------------------------------\n");

    ptr = tail;

    while(ptr != NULL){

        printf("%d -> ", ptr->data);

        ptr = ptr->prev;
    }

    printf("NULL");


    /*
        Complexity Analysis

        Forward Traversal:
        Time Complexity  : O(n)

        Backward Traversal:
        Time Complexity  : O(n)

        Extra Space:
        O(1)
    */

    printf("\n\nComplexity Analysis:\n");
    printf("-------------------\n");
    printf("Forward Traversal  : O(n)\n");
    printf("Backward Traversal : O(n)\n");
    printf("Extra Space        : O(1)\n");


    return 0;
}

