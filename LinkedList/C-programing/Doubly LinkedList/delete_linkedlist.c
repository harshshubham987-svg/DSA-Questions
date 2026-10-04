/*
    ============================================================
                    DOUBLY LINKED LIST
                    DELETION OPERATIONS
    ============================================================

    This program demonstrates:

        1. Forward traversal
        2. Backward traversal
        3. Delete node from beginning
        4. Delete node from end
        5. Delete node from a specific position

    Example:

        Original:
        1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6

        Forward:
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL

        Backward:
        6 -> 5 -> 4 -> 3 -> 2 -> 1 -> NULL
*/


#include <stdio.h>
#include <stdlib.h>


/*
    ============================================================
                    NODE STRUCTURE
    ============================================================

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
    ============================================================
                    TRAVERSE FORWARD
    ============================================================

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
    ============================================================
                    TRAVERSE BACKWARD
    ============================================================

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


/*
    ============================================================
                    DELETE FROM BEGINNING
    ============================================================

    Purpose:
        Deletes the first node of the doubly linked list.

    Steps:
        1. Store the current head in temp.
        2. Move head to the next node.
        3. Update the new head's prev pointer.
        4. Free the old head.
*/
void delete_from_begning(struct Node** head){

    struct Node* temp = *head;

    *head = temp->next;

    temp->next->prev = NULL;

    free(temp);

    printf("After Deleting From Beginning:\n");
    printf("--------------------------------\n");

    traverse_forward(head);
}


/*
    ============================================================
                DELETE FROM SPECIFIC POSITION
    ============================================================

    Purpose:
        Deletes the node present at the given position.

    Cases handled:
        1. Invalid / empty linked list
        2. First node
        3. Last node
        4. Middle node
*/
void delete_from_specificPlace(struct Node** head, int pos){

    if(*head == NULL){

        printf("\n\nLinked List IS Empty!\n");

        return;
    }

    struct Node* ptr = *head;
    struct Node* temp = NULL;

    int curr_pos = 0;


    /*
        Position 0 is not handled by this operation.
    */
    if(pos == 0){

        printf("\nPlease Enter the valid Position.\n");

        return;
    }


    /*
        Find the node at the given position.
    */
    while(ptr != NULL && curr_pos != pos){

        temp = ptr;

        curr_pos++;

        ptr = ptr->next;
    }


    /*
        Check whether the given position is valid.
    */
    if(curr_pos != pos){

        printf("\n\nInvald Linked List Postion\n");

        return;
    }


    /*
        Case 1:
        Deleting the first node.
    */
    if(temp->prev == NULL){

        *head = temp->next;

        temp->next->prev = NULL;

        free(temp);
    }


    /*
        Case 2:
        Deleting the last node.
    */
    else if(temp->next == NULL){

        temp->prev->next = NULL;

        free(temp);
    }


    /*
        Case 3:
        Deleting a middle node.
    */
    else{

        temp->prev->next = temp->next;

        temp->next->prev = temp->prev;

        free(temp);
    }


    printf("After Deleting From Specific Position:\n");
    printf("----------------------------------------\n");

    traverse_forward(head);
}


/*
    ============================================================
                    DELETE FROM END
    ============================================================

    Purpose:
        Deletes the last node of the doubly linked list.

    Steps:
        1. Store the current tail in temp.
        2. Move tail to the previous node.
        3. Update the new tail's next pointer.
        4. Free the old tail.
*/
void delete_from_end(struct Node** tail){

    struct Node* temp = *tail;

    *tail = temp->prev;

    temp->prev->next = NULL;

    free(temp);

    printf("After Deleting From End:\n");
    printf("-------------------------\n");

    traverse_backward(tail);
}


/*
    ============================================================
                            MAIN
    ============================================================
*/
int main(){

    /*
        ========================================================
                    CREATING NODE POINTERS
        ========================================================
    */

    struct Node* head = NULL;
    struct Node* sec = NULL;
    struct Node* third = NULL;
    struct Node* fourth = NULL;
    struct Node* fifth = NULL;
    struct Node* tail = NULL;


    /*
        ========================================================
                    DYNAMIC MEMORY ALLOCATION
        ========================================================
    */

    head = (struct Node*)malloc(sizeof(struct Node));
    sec = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    fourth = (struct Node*)malloc(sizeof(struct Node));
    fifth = (struct Node*)malloc(sizeof(struct Node));
    tail = (struct Node*)malloc(sizeof(struct Node));


    /*
        ========================================================
                    CREATING DOUBLY LINKED LIST
        ========================================================

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
        ========================================================
                    ORIGINAL LINKED LIST
        ========================================================
    */

    printf("Original Linked List:\n");
    printf("---------------------\n");

    traverse_forward(&head);


    /*
        ========================================================
                    DELETE FROM BEGINNING
        ========================================================
    */

    printf("\n\n");

    delete_from_begning(&head);


    /*
        ========================================================
                    DELETE FROM END
        ========================================================
    */

    printf("\n\n");

    delete_from_end(&tail);


    /*
        ========================================================
                DELETE FROM SPECIFIC POSITION
        ========================================================
    */

    printf("\n\n");

    delete_from_specificPlace(&head, 4);


    /*
        ========================================================
                    TIME COMPLEXITY
        ========================================================

        Forward Traversal:
            O(n)

        Backward Traversal:
            O(n)

        Delete From Beginning:
            O(1)

        Delete From End:
            O(1)

        Delete From Specific Position:
            O(n)

        Overall:
            O(n)
    */


    /*
        ========================================================
                    SPACE COMPLEXITY
        ========================================================

        Extra Space:
            O(1)

        No additional data structure is used.
    */


    return 0;
}