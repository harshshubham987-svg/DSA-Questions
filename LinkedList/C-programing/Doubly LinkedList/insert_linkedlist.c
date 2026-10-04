
#include <stdio.h>
#include <stdlib.h>


/*
    ============================================================
                    DOUBLY LINKED LIST
                    INSERTION OPERATIONS
    ============================================================

    Node contains:
        data -> stores the value
        next -> points to the next node
        prev -> points to the previous node
*/


/*
    ============================================================
                    NODE STRUCTURE
    ============================================================
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
                    INSERT NODE AT BEGINNING
    ============================================================

    A new node is inserted before the current head.
*/
void insert_node_begning(struct Node** head){

    struct Node* newNode = NULL;

    newNode = (struct Node*)malloc(sizeof(struct Node));

    struct Node* ptr = *head;

    newNode->data = 5;
    newNode->next = ptr;
    newNode->prev = NULL;

    ptr->prev = newNode;

    *head = newNode;

    printf("\n\nAfter Inserting Node at Beginning:\n");
    printf("-----------------------------------\n");

    traverse_forward(head);
}


/*
    ============================================================
                    INSERT NODE AT SPECIFIC PLACE
    ============================================================

    A new node is inserted before the node present
    at the given position.
*/
void insert_node_SpecificPlace(struct Node** head, int pos){

    struct Node* newNode = NULL;
    struct Node* temp = NULL;

    int curr_pos = 0;

    newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->data = 9;

    struct Node* ptr = *head;

    while(ptr != NULL && curr_pos != pos){

        temp = ptr;

        curr_pos++;

        ptr = ptr->next;
    }

    if(curr_pos != pos){

        printf("\n\nInvalid Position\n\n");

        free(newNode);

        return;
    }

    newNode->prev = temp->prev;

    newNode->next = temp;

    if(temp->prev != NULL){

        temp->prev->next = newNode;

    }else{

        *head = newNode;
    }

    temp->prev = newNode;

    printf("\n\nAfter Inserting Node at Specific Position:\n");
    printf("-------------------------------------------\n");

    traverse_forward(head);
}


/*
    ============================================================
                    INSERT NODE AT END
    ============================================================

    A new node is inserted after the current tail.
*/
void insert_node_end(struct Node** tail){

    struct Node* newNode = NULL;

    newNode = (struct Node*)malloc(sizeof(struct Node));

    struct Node* ptr = *tail;

    newNode->data = 7;
    newNode->next = NULL;
    newNode->prev = ptr;

    ptr->next = newNode;

    *tail = newNode;

    printf("\n\nAfter Inserting Node at End:\n");
    printf("----------------------------\n");

    traverse_backward(tail);
}


/*
    ============================================================
                            MAIN
    ============================================================
*/
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
        ========================================================
                    CREATING DOUBLY LINKED LIST
        ========================================================
    */

    head->prev = NULL;
    head->data = 1;
    head->next = sec;


    sec->prev = head;
    sec->data = 2;
    sec->next = third;


    third->prev = sec;
    third->data = 3;
    third->next = fourth;


    fourth->prev = third;
    fourth->data = 4;
    fourth->next = fifth;


    fifth->prev = fourth;
    fifth->data = 5;
    fifth->next = tail;


    tail->data = 6;
    tail->prev = fifth;
    tail->next = NULL;


    /*
        ========================================================
                    INSERTION OPERATIONS
        ========================================================
    */
    printf("Original Linked List:\n");
    printf("----------------------------\n");

    traverse_forward(&head);

    insert_node_begning(&head);

    insert_node_end(&tail);

    insert_node_SpecificPlace(&head, 6);


    /*
        ========================================================
                    TIME COMPLEXITY
        ========================================================

        Traverse Forward:
            O(n)

        Traverse Backward:
            O(n)

        Insert at Beginning:
            O(1)
            (excluding traversal)

        Insert at End:
            O(1)
            (tail pointer is already available)

        Insert at Specific Position:
            O(n)
            (we may need to traverse to the position)


        ========================================================
                    SPACE COMPLEXITY
        ========================================================

        Extra space used by insertion operations:
            O(1)

        Each newly inserted node requires:
            O(1) space
    */


    return 0;
}