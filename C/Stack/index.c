// Stack implementation in C

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 10

int count = 0;

// Creating a stack
typedef struct Stack
{
    int items[MAX];
    int top;
} Stack;

void createStack(Stack *s)
{
    s->top = -1;
}

// Check if the stack is full
bool isfull(Stack *s)
{
    if (s->top == MAX)
    {
        return true;
    }
    return false;
}

// Check if the stack is empty
bool isempty(Stack *s)
{
    if (s->top == -1)
    {
        return true;
    }
    return false;
}
// Add elements into stack
void push(Stack *s, int item)
{
    if (isfull(s))
    {
        printf("STACK FULL");
    }
    else
    {
        s->top++;
        s->items[s->top] = item;
    }
    count++;
}

// Remove element from stack
void pop(Stack *s)
{
    if (isempty(s))
    {
        printf("STACK EMPTY");
    }
    else
    {
        printf("Item popped = %d \n", s->items[s->top]);
        s->items[s->top] = NULL;
        s->top--;

    }
    count--;
}

// Print elements of stack
void printStack(Stack *s)
{
    printf("Stack: ");
    for (int i = 0; i < count; i++)
    {
        printf("%d ", s->items[i]);
    }
    printf("\n");
}

// Driver code
int main()
{
    int ch;
    Stack *s = (Stack *)malloc(sizeof(Stack));

    createStack(s);

    push(s, 1);
    push(s, 2);
    push(s, 3);
    push(s, 4);

    printStack(s);

    pop(s);
    pop(s);

    printf("\nAfter popping out\n");
    printStack(s);
    free(s);
}
