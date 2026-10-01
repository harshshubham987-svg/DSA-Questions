/*
    Doubly Linked List Traversal Using Recursion

    This program demonstrates:

    1. Forward traversal using recursion
    2. Backward traversal using recursion

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
    Function: recursion_forward

    Purpose:
    Traverses the Doubly Linked List from
    head to tail using recursion.

    The function moves through the list
    using the next pointer.
*/
void recursion_forward(struct Node** head){

    struct Node* ptr = *head;


    /*
        Base Case:
        If the current node is NULL,
        the traversal is complete.
    */
    if(ptr == NULL){

        printf("NULL");
        return;
    }


    /*
        Print the current node's data
    */
    printf("%d -> ", ptr->data);


    /*
        Recursive Call:
        Move to the next node
    */
    recursion_forward(&(ptr->next));
}


/*
    Function: recursion_backward

    Purpose:
    Traverses the Doubly Linked List from
    tail to head using recursion.

    The function moves through the list
    using the prev pointer.
*/
void recursion_backward(struct Node** tail){

    struct Node* ptr = *tail;


    /*
        Base Case:
        If the current node is NULL,
        the traversal is complete.
    */
    if(ptr == NULL){

        printf("NULL");
        return;
    }


    /*
        Print the current node's data
    */
    printf("%d -> ", ptr->data);


    /*
        Recursive Call:
        Move to the previous node
    */
    recursion_backward(&(ptr->prev));
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
        Forward Traversal Using Recursion

        Start from head and recursively
        follow the next pointer.
    */
    printf("Moving Forward ------->\n");
    printf("--------------------------------------------\n");

    recursion_forward(&head);


    /*
        Backward Traversal Using Recursion

        Start from tail and recursively
        follow the prev pointer.
    */
    printf("\n\nMoving from Backward ------->\n");
    printf("--------------------------------------------\n");

    recursion_backward(&tail);


    /*
        Complexity Analysis

        Forward Traversal:
        Time Complexity  : O(n)
        Recursive Space  : O(n)

        Backward Traversal:
        Time Complexity  : O(n)
        Recursive Space  : O(n)

        The O(n) space is due to the
        recursive call stack.
    */

    printf("\n\nComplexity Analysis:\n");
    printf("-------------------\n");
    printf("Forward Traversal  : O(n) Time, O(n) Space\n");
    printf("Backward Traversal : O(n) Time, O(n) Space\n");


    return 0;
}

