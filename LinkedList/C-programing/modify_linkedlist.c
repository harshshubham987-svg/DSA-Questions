/*
    Problem:

    Modify a singly linked list by processing nodes in pairs
    from both ends.

    For each pair:
        new first value = last value - original first value
        new last value  = original first value

    For an odd-length linked list, the middle node
    remains unchanged.

    Example:

    Input:
    10 -> 4 -> 5 -> 3 -> 6

    Output:
    -4 -> -1 -> 5 -> 4 -> 10
*/

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
    Function: traverse

    Purpose:
    Traverses the linked list and displays
    all node values.
*/
void traverse(struct Node** head){

    struct Node* ptr = *head;

    while(ptr != NULL){
        printf("%d -> ", ptr->data);
        ptr = ptr->next;
    }

    printf("NULL");
}


/*
    Function: modify_linkedlist

    Purpose:
    Processes the linked list from both ends
    and modifies the node values according to
    the given condition.
*/
void modify_linkedlist(struct Node** head){

    int arr[100];

    struct Node* ptr = *head;

    int count = 0;


    /*
        Store all linked list values
        inside an array.
    */
    while(ptr != NULL){

        arr[count] = ptr->data;
        count++;

        ptr = ptr->next;
    }


    /*
        Process the array from both ends.

        first -> points to the first element
        last  -> points to the last element
    */
    int first = 0;
    int last = count - 1;


    while(first < last){

        /*
            Store the original first value
            before modifying it.
        */
        int temp = arr[first];

        /*
            New first value:
            last value - original first value
        */
        arr[first] = arr[last] - arr[first];

        /*
            New last value:
            original first value
        */
        arr[last] = temp;

        first++;
        last--;
    }


    /*
        Copy the modified values back
        into the linked list.
    */
    int indx = 0;

    ptr = *head;

    while(ptr != NULL){

        ptr->data = arr[indx];

        ptr = ptr->next;
        indx++;
    }


    /*
        Display the modified linked list.
    */
    traverse(head);
}


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
        for each node.
    */
    head = (struct Node*)malloc(sizeof(struct Node));
    sec = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    four = (struct Node*)malloc(sizeof(struct Node));
    fifth = (struct Node*)malloc(sizeof(struct Node));


    /*
        Creating the Linked List

        10 -> 4 -> 5 -> 3 -> 6 -> NULL
    */

    head->data = 10;
    head->next = sec;

    sec->data = 4;
    sec->next = third;

    third->data = 5;
    third->next = four;

    four->data = 3;
    four->next = fifth;

    fifth->data = 6;
    fifth->next = NULL;


    /*
        Display Original Linked List
    */
    printf("Original Linked List:\n");
    printf("---------------------\n");

    traverse(&head);


    /*
        Modify the Linked List
    */
    printf("\n\nAfter Modification Linked List:\n");
    printf("--------------------------------\n");

    modify_linkedlist(&head);


    /*
        Complexity Analysis

        Let n be the number of nodes.

        Time Complexity:
        O(n)

        The linked list is traversed to store the values,
        processed from both ends, and traversed again
        to update the nodes.

        Space Complexity:
        O(n)

        An auxiliary array is used to store the
        linked list values.
    */

    printf("\n\nComplexity Analysis:\n");
    printf("-------------------\n");
    printf("Time Complexity  : O(n)\n");
    printf("Space Complexity : O(n)\n");


    return 0;
}

